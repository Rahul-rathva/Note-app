from sqlmodel import Session, select
from app.db import engine
from app.models import Note

def create_note(title: str, content: str) -> Note:
    with Session(engine) as session:
        note = Note(title=title, content=content)
        session.add(note)
        session.commit()
        session.refresh(note)
        return note
        
def get_notes():
    with Session(enigne) as sesssion:
        satatement = select(Note)
        results=session.exec(statement)
        return  results.all()
