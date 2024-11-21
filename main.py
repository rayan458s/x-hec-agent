from typing import Union
from pydantic import BaseModel
from openai import OpenAI
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
app = FastAPI()


# Message model
class Message(BaseModel):
    message: str


@app.get("/")
def read_root():
    return {"Hello": "PLB!"}


@app.post("/message")
def send_message(request: Message):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are Bruno Martinaud. Talk about your experience with OpenAI.",
            },
            {"role": "user", "content": request.message},
        ],
    )

    answer = completion.choices[0].message.content

    return {"answer": answer}
