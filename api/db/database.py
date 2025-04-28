import os
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy import URL
from sqlmodel import Session, SQLModel, create_engine

load_dotenv()


DB_HOST = os.getenv("DB_HOST", "")
DB_NAME = os.getenv("DB_NAME", "")
USERNAME = os.getenv("DB_USERNAME", "")
PASSWORD = os.getenv("DB_PASSWORD", "")
PORT = os.getenv("DB_PORT", "")

DATABASE_URL = URL.create(
    drivername="postgresql",
    host=DB_HOST,
    username=USERNAME,
    password=PASSWORD,
    port=PORT,
    database=DB_NAME,
)
print("db url: ", DATABASE_URL.render_as_string(hide_password=False))

# allow FastAPI to use the same database in different threads
# Necessary b/c one single request could use multiple threads
connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL)
# engine = create_engine(
#     "postgresql://postgres:tango9ij(IJ@refetch.cr04sckw0441.us-east-1.rds.amazonaws.com:5432/postgres"
# )


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
