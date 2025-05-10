import os
import ssl
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy import URL
from sqlmodel import Session, SQLModel, create_engine

# Necessary so SQLModel can create the tables
from api import models  # pylint: disable=unused-import

load_dotenv()


DB_HOST = os.getenv("DB_HOST", "")
DB_NAME = os.getenv("DB_NAME", "")
USERNAME = os.getenv("DB_USERNAME", "")
PASSWORD = os.getenv("DB_PASSWORD", "")
PORT = os.getenv("DB_PORT", "")

DATABASE_URL = URL.create(
    drivername="postgresql+pg8000",
    host=DB_HOST,
    username=USERNAME,
    password=PASSWORD,
    port=PORT,
    database=DB_NAME,
)

pem_path = os.path.abspath("api/certs/us-east-1-bundle.pem")
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.load_verify_locations(pem_path)
# allow FastAPI to use the same database in different threads
# Necessary b/c one single request could use multiple threads
db_args = {
    "timeout": 5,
    "ssl_context": ssl_context,
}

engine = create_engine(DATABASE_URL, connect_args=db_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
