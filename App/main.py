from fastapi import FastAPI
from app.db import create_db_and_tables
from app.crud import create_note, get_notes

app = FastAPI(title="Notes API")

@app.get("/")
def root():
    return {"message": "Welcome to the Notes API"}

@app.on_event("startup")
def on_statup():
    create_db_and_tables()

@app.post("/notes/", response_model=Note)
def create_note_endpoint(note: Note):
    return create_note(note)

def list_notes():
    return get_notes()