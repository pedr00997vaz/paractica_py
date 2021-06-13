from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello" : "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q" : q}

@app.get("/user/{usr_name}")
def read_user(usr_name: str, age: int, matricula: int):
    return {"usr_name": usr_name, "20" : age, "091.." : matricula}
