# 📝 Note-App — Fast, Reliable REST API for Notes

A compact, production-minded backend built with **FastAPI** and **SQLModel** to create, read, update, and manage notes quickly and safely. Designed for clarity, testability, and easy extension.

---

## Key Highlights

- FastAPI + SQLModel for robust request validation and clean ORM
- SQLite for zero-config local development (easy to swap to Postgres)
- Clear separation: routes, models, DB, and CRUD logic
- Live API docs at /docs when running locally
- Lightweight and ready for CI, tests, and deployment

---

## Contents

- [App/main.py](App/main.py) — application entry, routes and startup
- [App/models.py](App/models.py) — Pydantic/SQLModel models
- [App/crud.py](App/crud.py) — database operations (Create / Read / Update / Delete)
- [App/db.py](App/db.py) — DB engine and session setup
- [README.md](README.md) — this file

---

## Quickstart (local)

1. Clone and enter repo
   ```bash
   git clone https://github.com/Rahul-rathva/Note-app.git
   cd Note-App```

### Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Linux/Mac


Install dependencies
pip install fastapi uvicorn sqlmodel

Run the server
uvicorn App.main:app --reload

Open in browser

Go to: http://127.0.0.1:8000/docs

Explore and test all endpoints interactively using Swagger UI.

🧩 Example API Calls
➕ Create a Note

POST /notes/

{
  "title": "Learn FastAPI",
  "content": "My first working API!"
}

📜 Get All Notes

GET /notes/

Response:

[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "content": "My first working API!"
  }
]

🧠 Future Improvements

🔐 Add JWT authentication (login/register)

🗃️ Switch to PostgreSQL for production

🧪 Add pytest-based unit testing

☁️ Deploy on Render or Railway

🧱 Implement full CRUD (Update & Delete)


⭐ How to Support

If you found this project helpful:

Give it a ⭐ on GitHub

Fork it and try adding new features

Share it with others learning backend development

