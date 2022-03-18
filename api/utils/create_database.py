from typing import Callable

import loguru

from api.db import engine, Base
from api.db.models import HomeContent, Social, Post, Tag, Admin, Project
from api.utils.populate_db import populate_database, populate_projects,\
    populate_admin, populate_socials, populate_tags, populate_posts, populate_home_contents


def init_db():
    loguru.logger.info("Dropping database...")
    Base.metadata.drop_all(engine)

    loguru.logger.info("Creating database...")
    Base.metadata.create_all(engine)

    loguru.logger.info("Populating database...")
    populate_database()


def populate():
    print("""
    Choose a model to populate: \n
    [0] - All
    [1] - Admin
    [2] - HomeContent
    [3] - Post
    [4] - Project
    [5] - Social
    [6] - Tag
    """)

    option = int(input(": "))
    if not isinstance(option, int):
        print("You should to pass a number.")
        option = int(input(": "))

    functions = [
        init_db,
        populate_admin,
        populate_home_contents,
        populate_posts,
        populate_projects,
        populate_socials,
        populate_tags
    ]

    functions[option]()


populate()
