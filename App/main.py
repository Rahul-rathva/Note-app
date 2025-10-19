from fastapi import FastAPI

app = FastAPI(title="Notes API")

@app.get("/")
def root():
    return {"message": "My name is Rahul"}
    return {"message": "Welcome to the Notes API"}
