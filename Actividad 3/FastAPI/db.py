from sqlmodel import Session, create_engine, SQLModel
import os
from fastapi import Depends, FastAPI
from dotenv import load_dotenv
from typing import Annotated

load_dotenv()

mysql_url = os.getenv("DATABASE_URL")
print("Conectando a:", mysql_url)  # Debug para ver si se está cargando bien

if not mysql_url:
    raise Exception("DATABASE_URL not set")

engine = create_engine(mysql_url, echo=True)  # echo=True para ver las consultas en consola

def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]