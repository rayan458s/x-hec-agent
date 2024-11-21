from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()


def my_agent(message: str) -> str:
    return "Hello, " + message + "!"


# Message model
class Message(BaseModel):
    message: str


@app.get("/")
def read_root():
    return {"Hello": "PLB!"}


@app.post("/message")
def send_message(request: Message):
    response = my_agent(request.message)

    return {"message": response}
