import os
import glob
import base64
import random
import fastapi
import uvicorn
import openai
import requests
import logging
from PyPDF2 import PdfReader
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

PDF_FILE = glob.glob("portfolio/public/*.pdf")[0]
RESUME = " ".join(
    " ".join([page.extract_text() for page in PdfReader(PDF_FILE).pages]).split()
)

AUTHOR_FIRST_NAME, AUTHOR_LAST_NAME = os.getenv(
    "AUTHOR_FIRST_NAME", "Peter"
), os.getenv("AUTHOR_LAST_NAME", "Jung")
AUTHOR_LOCATION = os.getenv("AUTHOR_LOCATION", "Prague, Czech Republic")
SYSTEM_MESSAGE = {
    "role": "system",
    "content": f"""You are a resume bot developed by {AUTHOR_FIRST_NAME} {AUTHOR_LAST_NAME}.
You have {AUTHOR_FIRST_NAME} {AUTHOR_LAST_NAME}'s resume and you can answer questions about it.
{AUTHOR_FIRST_NAME} has an international experience, but currently resides in {AUTHOR_LOCATION}.
Assume you are talking with a colleague, a friend, a employer or a potentional employer of {AUTHOR_FIRST_NAME}.
Answer in concise but full sentences. Make {AUTHOR_FIRST_NAME} look good and be funny.

This is {AUTHOR_FIRST_NAME}'s resume:
```
{RESUME}
```
""",
}
IMAGE_DIR = "photobooth/jung"
# This is meant to be a simple portfolio with a single deployment,
# so we can use a global variable to store the chat history without any problems.
MEMORY = {}


def create_app():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    app = fastapi.FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            x_stripped
            for x in os.getenv(
                "ALLOW_ORIGINS",
                "https://jung.ninja,https://www.jung.ninja,http://localhost:4000",
            ).split(",")
            if (x_stripped := x.strip())
        ],
        allow_methods=["GET", "POST"],
    )

    @app.post("/log/")
    def _log(
        request: fastapi.Request,
        user_id: str = fastapi.Body(..., embed=True),
        version: str = fastapi.Body(..., embed=True),
        question: str = fastapi.Body(..., embed=True),
        answer: str = fastapi.Body(..., embed=True),
    ):
        send_slack_message(
            f"""From: `{user_id}` ({get_client_info(request)})
Version: `{version}`
Question: `{question}`
Answer:
```
{answer}
```"""
        )

    @app.get("/ask/")
    def _ask(
        user_id: str,
        question: str,
    ):
        messages = MEMORY.get(user_id, [SYSTEM_MESSAGE])
        messages = messages + [{"role": "user", "content": question}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.5,
            top_p=1,
            n=1,
            max_tokens=500,
        )
        answer = dict(response.choices[0]["message"])
        MEMORY[user_id] = messages + [answer]
        return {"answer": answer["content"]}

    @app.get("/photo/")
    def _photo(
        request: fastapi.Request,
        user_id: str,
        prompt: str,
    ):
        choices = os.listdir(IMAGE_DIR)
        chosen = random.choice(choices)
        with open(f"{IMAGE_DIR}/{chosen}", "rb") as f:
            response = openai.Image.create_edit(
                image=f,
                prompt=prompt,
                n=1,
                size="512x512",
            )
        image_url = response.data[0]["url"]
        send_slack_message(
            f"""From: `{user_id}` ({get_client_info(request)})
Prompt: `{prompt}`
Answer: {image_url}"""
        )
        content = requests.get(image_url).content
        base64_encoded_image = base64.b64encode(content).decode("utf-8")
        return {"image": base64_encoded_image}

    return app


def get_ip_info(ip: str) -> str:
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        response_json = response.json()
        return ", ".join(f"{k}={v}" for k, v in response_json.items())
    except Exception as e:
        return f"Error: {e}"


def get_client_info(request: fastapi.Request) -> str:
    x_real_ip = request.headers.get("do-connecting-ip")
    return (
        f"""{x_real_ip=}, {get_ip_info(x_real_ip)}"""
        if x_real_ip
        else f"Unknown: `{x_real_ip}`"
    )


def send_slack_message(text: str) -> None:
    SLACK_TOKEN = os.environ.get("SLACK_TOKEN")
    SLACK_NOTIFY_USER = os.environ.get("SLACK_NOTIFY_USER")

    if not (SLACK_TOKEN and SLACK_NOTIFY_USER):
        logging.error("No Slack token or user to notify, skipping.")
        return

    requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={
            "Content-type": "application/json",
            "Authorization": f"Bearer {SLACK_TOKEN}",
        },
        json={
            "channel": SLACK_NOTIFY_USER,
            "link_names": True,
            "text": text,
        },
    )


if __name__ == "__main__":
    uvicorn.run(
        "api:create_app",
        factory=True,
        host="0.0.0.0",
        port=4001,
        workers=1,
        reload=True,
        log_level="debug",
    )
