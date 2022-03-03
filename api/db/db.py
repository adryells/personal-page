from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

BASE_DIRECTORY = os.path.join(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URL = f'sqlite:///{os.path.join(BASE_DIRECTORY, "database.db")}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True, future=True
    )

# TODO: to understend autoflush
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
Base = declarative_base()


def get_session() -> Session:
    return session