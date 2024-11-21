from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()


# Message model
class Message(BaseModel):
    message: str


@app.get("/")
def read_root():
    return {"Hello": "PLB!"}


@app.post("/message")
def send_message(request: Message):
    return {"message": request.message}
