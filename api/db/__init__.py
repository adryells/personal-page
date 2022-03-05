from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

BASE_DIRECTORY = os.path.join(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URL = f'sqlite:///{os.path.join(BASE_DIRECTORY, "../../database.db")}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    )

SessionLocal = sessionmaker(bind=engine, autoflush=False)
session = SessionLocal()
Base = declarative_base()


def get_session() -> Iterator[Session]:
    db_session: Session = SessionLocal()

    try:
        yield db_session
    finally:
        db_session.close()