from fastapi import APIRouter
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models.note import Note
from config.db import conn
from schemas.note import notes, NoteEntity

note = APIRouter()

note.mount("/static", StaticFiles(directory="static"), name="static")
#Templates
templates = Jinja2Templates(directory="templates")



@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newdocs = []
    for doc in docs:
        newdocs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"],
            "important" : doc["important"]

        })
    # print(docs)
    return templates.TemplateResponse("index.html", {"request": request,"newdocs":newdocs})





@note.post("/")
async def create_note(request:Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict["important"] == "on" else False
    inserted_note = conn.notes.notes.insert_one(dict(formDict))
    print(inserted_note)
    return  {"sucess":True}

