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



