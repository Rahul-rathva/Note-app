from sqlmodel import SQLModel, Session, create_engine

# Step 1: Create engine (connect to DB)
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)  # echo=True shows SQL logs

# Step 2: Function to create tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Step 3: Dependency for creating DB sessions
def get_session():
    with Session(engine) as session:
        yield session
