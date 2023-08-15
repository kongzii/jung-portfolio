import os
import base64
import random
import fastapi
import uvicorn
import openai
import requests
import logging
from pprint import pprint
from PyPDF2 import PdfReader
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

resume = " ".join(
    " ".join(
        [
            page.extract_text()
            for page in PdfReader(
                "portfolio/public/Peter_Jung_CV_extended.pdf"
                if os.path.isfile("portfolio/public/Peter_Jung_CV_extended.pdf")
                else "public/Peter_Jung_CV_extended.pdf"
            ).pages
        ]
    ).split()
)

load_dotenv()


SYSTEM_MESSAGE = {
    "role": "system",
    "content": f"""You are a resume bot developed by Peter Jung.
You have Peter Jung's resume and you can answer questions about it.
Peter has an international experience, but currently resides in Prague, Czech Republic.
Assume you are talking with a potential employer for Peter.
Answer in concise but full sentences. Make Peter look good and be funny.

This is Peter's resume:
```
{resume}
```
""",
}
MEMORY = {}


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


def create_app():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    app = fastapi.FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "https://jung.ninja",
            "https://www.jung.ninja",
            "http://localhost:4000",
        ],
        allow_methods=["POST"],
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
        # pprint(MEMORY[user_id])
        return {"answer": answer["content"]}

    @app.get("/photo/")
    def _photo(
        request: fastapi.Request,
        user_id: str,
        prompt: str,
    ):
        image_dir = "photobooth/jung" if os.path.isdir("photobooth/jung") else "jung"
        choices = os.listdir(image_dir)
        chosen = random.choice(choices)
        with open(f"{image_dir}/{chosen}", "rb") as f:
            response = openai.Image.create_edit(
                image=f,
                prompt=prompt,
                n=1,
                size="512x512",
            )
        image_url = response.data[0]["url"]
        # image_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-jSJe7fmVAf6zXbI4porb6Ttl/user-cQ4Q7qDCTNdUwM8zGkRyoVaw/img-iMNN5RgixmEN0nD22SsHe7xK.png?st=2023-07-30T14%3A03%3A26Z&se=2023-07-30T16%3A03%3A26Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-07-30T08%3A36%3A40Z&ske=2023-07-31T08%3A36%3A40Z&sks=b&skv=2021-08-06&sig=OaC7wU4Mnh5XfueoguIt2GhTiW2oJU9vl7q6J%2Buz%2Bvs%3D"
        send_slack_message(
            f"""From: `{user_id}` ({get_client_info(request)})
Prompt: `{prompt}`
Answer: {image_url}"""
        )
        content = requests.get(image_url).content
        base64_encoded_image = base64.b64encode(content).decode("utf-8")
        return {"image": base64_encoded_image}

    return app


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
