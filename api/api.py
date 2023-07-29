import os
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
            for page in PdfReader("portfolio/public/Peter_Jung_CV_extended.pdf").pages
        ]
    ).split()
)

load_dotenv()


SYSTEM_MESSAGE = {
    "role": "system",
    "content": f"""You are a resume bot developed by Peter Jung.
You have Peter Jung's resume and you can answer questions about it.
Assume you are talking with a potential employer for Peter.
Answer in short sentences and short answers. Don't forget to make Peter look good.
Be a little funny sometimes.
If user doesn't ask in form of a question, talk about something similar from the resume.

This is Peter's resume:
```
{resume}
```
""",
}
MEMORY = {}


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
        user_id: str = fastapi.Body(..., embed=True),
        version: str = fastapi.Body(..., embed=True),
        question: str = fastapi.Body(..., embed=True),
        answer: str = fastapi.Body(..., embed=True),
    ):
        send_slack_message(
            f"""From: `{user_id}`
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
            temperature=0,
            top_p=1,
            n=1,
            max_tokens=300,
        )
        answer = dict(response.choices[0]["message"])
        MEMORY[user_id] = messages + [answer]
        pprint(MEMORY[user_id])
        return {"answer": answer["content"]}

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
