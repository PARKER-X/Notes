#Import
from typing import Union
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

#App
app = FastAPI()
#Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")
#Templates
templates = Jinja2Templates(directory="templates")


#Mongo Connection
conn = MongoClient("mongodb+srv://Parker:parker1234@notesapp.fbynitg.mongodb.net/")



@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newdocs = []
    for doc in docs:
        newdocs.append({
            "id": doc["_id"],
            "note": doc["note"]

        })
    # print(docs)
    return templates.TemplateResponse("index.html", {"request": request,"newdocs":newdocs})

