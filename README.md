# 📝 Notes API — Fast, Simple & Modern REST API  

A lightweight **backend application** built with **FastAPI** and **SQLModel**, designed for creating and managing digital notes with ease.  

This project demonstrates how to build a **production-ready REST API** from scratch using modern Python tools — combining **speed**, **clarity**, and **real-world structure**.  

---

## 🚀 Features  

- ⚡ **FastAPI Framework** — High performance, easy to learn, async-ready  
- 🧱 **SQLModel ORM** — Combines Pydantic + SQLAlchemy for simplicity  
- 💾 **SQLite Database** — Lightweight and perfect for development  
- 📖 **Automatic Swagger UI Docs** at `/docs`  
- 🔁 Supports **CRUD operations** (Create, Read — Update & Delete coming soon)  
- 🧩 Clean modular structure following professional backend practices  
- 🌱 Ready for integration with **PostgreSQL** and **JWT Authentication**  

---

## 🧠 What You’ll Learn  

By building and exploring this project, you’ll understand:  
- How APIs handle client requests and respond with JSON  
- How FastAPI validates and processes data automatically  
- How to connect applications to databases using ORM  
- How CRUD logic works with sessions and commits  
- How to structure backend code for scalability  
- How to debug common backend issues in real projects  

---

## 🏗️ Tech Stack  

| Category | Technology | Why |
|-----------|-------------|-----|
| Backend Framework | [FastAPI](https://fastapi.tiangolo.com/) | Modern, fast, async-ready |
| ORM & Validation | [SQLModel](https://sqlmodel.tiangolo.com/) | Combines SQLAlchemy & Pydantic |
| Database | SQLite | Lightweight, no external setup |
| Server | [Uvicorn](https://www.uvicorn.org/) | ASGI server for FastAPI |
| Language | Python 3.8+ | Clean, beginner-friendly, widely used |

---

## 📂 Project Structure  

```
Note-App/
 └── App/
      ├── main.py         # Entry point — defines routes & startup events
      ├── models.py       # Data models & table definitions
      ├── crud.py         # Create/Read operations using SQLModel sessions
      ├── db.py           # Database connection & session management
      ├── __init__.py     # Makes App a Python package
```

---

## ⚙️ Setup Instructions  

### 1️⃣ Clone this repository  
```bash
git clone https://github.com/rahulrathwa/Notes-API.git
cd Notes-API
```

### 2️⃣ Create and activate a virtual environment  
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Linux/Mac
```

### 3️⃣ Install dependencies  
```bash
pip install fastapi uvicorn sqlmodel
```

### 4️⃣ Run the server  
```bash
uvicorn App.main:app --reload
```

### 5️⃣ Open the interactive API docs  
Visit → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
Use the Swagger UI to test all endpoints visually.

---

## 🧩 Example API Calls  

### ➕ Create a Note  
**POST** `/notes/`  
**Request Body:**  
```json
{
  "title": "Learn FastAPI",
  "content": "This is my first API!"
}
```

**Response:**  
```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "content": "This is my first API!"
}
```

---

### 📜 Get All Notes  
**GET** `/notes/`

**Response:**  
```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "content": "This is my first API!"
  }
]
```

---

## 🧰 Common Issues & Fixes  

| Error | Reason | Fix |
|--------|--------|-----|
| `ModuleNotFoundError: No module named 'App'` | Folder name mismatch | Run from project root and check `App` spelling |
| `OperationalError: no such table` | Tables not created yet | Ensure `create_db_and_tables()` runs at startup |
| `422 Validation Error` | Invalid JSON input | Check field names and data types |
| `500 Internal Server Error` | Code crash or wrong imports | Read traceback and correct file paths |
| `ImportError: cannot import name 'Sessions'` | Typo in import | Use `Session` (singular) |

---

## 🧠 Future Enhancements  

- 🔐 Add **JWT Authentication** (login/register system)  
- 🗃️ Migrate to **PostgreSQL** for production use  
- 🧪 Add **pytest-based automated tests**  
- ☁️ Deploy the API on **Render, Railway, or Deta**  
- 🧱 Implement **Update & Delete** endpoints  
- 🌍 Add **CORS middleware** for frontend integration  

---

## ⭐ Support  

If you found this project helpful:  
- Star ⭐ the repository  
- Fork 🍴 it and add your improvements  
- Share it to help others learn backend development  

---

## 🧾 Summary  

> This Notes API is your gateway to learning backend development the **right way** — by building real, working systems with modern tools.  
> You’ll understand APIs, databases, validation, sessions, CRUD logic, and project structuring — everything that real backend developers do every day.  
