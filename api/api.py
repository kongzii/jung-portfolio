import os
import fastapi
import uvicorn
import openai
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

This is Peter's resume:
```
{resume}
```
""",
}
MEMORY = {}


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
        )
        answer = dict(response.choices[0]["message"])
        MEMORY[user_id] = messages + [answer]
        pprint(MEMORY[user_id])
        return answer["content"]

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
