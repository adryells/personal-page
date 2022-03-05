from api.db import engine, Base
from api.db.models import HomeContent, Social, Post, Tag, Admin, Project


def init_db():
    Base.metadata.create_all(engine)