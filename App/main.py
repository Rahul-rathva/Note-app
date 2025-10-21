from fastapi import FastAPI
from app.db import create_db_and_tables

app = FastAPI(title="Notes API")

@app.get("/")
def root():
    return {"message": "Welcome to the Notes API"}

@app.on_event("startup")
def on_statup():
    create_db_and_tables()