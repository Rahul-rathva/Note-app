# 📝 Notes APP — Fast, Simple & Modern REST API

A lightweight **backend application** built with **FastAPI** and **SQLModel**, designed for creating, reading, updating, and managing digital notes with ease.

This project demonstrates how to build a production-ready REST API from scratch using modern Python tools — combining **speed**, **clarity**, and **real-world structure**.

---

## 🚀 Features

- ⚡ Built with **FastAPI** — lightning-fast, modern Python web framework  
- 🧱 **SQLModel ORM** — combines Pydantic + SQLAlchemy for cleaner code  
- 💾 **SQLite Database** — easy to set up and perfect for local testing  
- 📖 **Automatic API Docs** — explore endpoints instantly at `/docs` (Swagger UI)  
- 🔁 Implements **CRUD operations** (Create, Read, Update, Delete)  
- 🧩 Clean folder structure following professional backend design principles  
- 🔐 Ready for integration with **PostgreSQL** and **JWT Authentication** (future-ready)

---

## 🧠 What You’ll Learn

This project helps you understand:
- How APIs receive requests, validate data, and return structured JSON responses  
- How backends communicate with databases using ORM (SQLModel)  
- How sessions, commits, and transactions work  
- How to organize scalable backend projects  
- How to debug common backend issues  

---

## 🏗️ Tech Stack

| Category | Technology | Why |
|-----------|-------------|-----|
| Backend Framework | [FastAPI](https://fastapi.tiangolo.com/) | Fast, async, automatic validation |
| ORM & Validation | [SQLModel](https://sqlmodel.tiangolo.com/) | Combines Pydantic & SQLAlchemy |
| Database | SQLite | Lightweight, great for learning |
| Server | [Uvicorn](https://www.uvicorn.org/) | ASGI server to run FastAPI |
| Language | Python 3.8+ | Simple, powerful, beginner-friendly |

---

## 📂 Project 

Note-App/
└── App/
├── main.py # Entry point — defines routes & startup events
├── models.py # Database table & data validation models
├── crud.py # Handles Create/Read logic using SQLModel sessions
├── db.py # Database connection and session management
├── init.py # Makes App a package


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Rahul-rathva/Note-app.git
cd Notes-App

### Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Linux/Mac



