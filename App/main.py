from fastapi import FastAPI
from App.db import create_db_and_tables
from App.crud import create_note, get_notes
from App.models import Note   

app = FastAPI(title="Notes API")

@app.get("/")
def root():
    return {"message": "Welcome to the Notes API"}

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/notes/", response_model=Note)
def create_note_endpoint(note: Note):
    return create_note(note)

@app.get("/notes/")
def list_notes():
    return get_notes()
