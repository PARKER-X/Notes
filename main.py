#Import
from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


#App
app = FastAPI()
#Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
