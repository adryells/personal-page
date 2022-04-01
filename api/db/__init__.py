from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from api.utils.settings import GeneralSettings

settings = GeneralSettings()

engine = create_engine(
    settings.DB_URL
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
