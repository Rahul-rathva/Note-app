from sqlmodel import SQLModel,Sessions,create_engine

sqlite_file_name="database.db"
sqlite_url=f"sqlite:////    {sqlite_file_name}"
engine=create_engine(sqlite_url,echo=true)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)