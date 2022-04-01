
import loguru
from sqlalchemy.engine import Engine

from api.db import engine, Base
from api.db.models import HomeContent, Social, Post, Tag, Admin, Project
from api.utils.populate_db import populate_projects,\
    populate_admin, populate_socials, populate_tags, populate_posts, populate_home_contents


class DBManager:

    def drop_all_tables(self, engine_: Engine):
        loguru.logger.info("Dropping database...")
        Base.metadata.drop_all(engine_ or engine)

    def create_all_tables(self, engine_: Engine, populate: bool = True):
        loguru.logger.info("Creating database...")
        Base.metadata.create_all(engine_ or engine)

        if populate:
            self.populate()

    def init_db(self, engine_: Engine):
        self.drop_all_tables(engine_ or engine)
        self.create_all_tables(engine_ or engine)

    def populate(self, option: int = 0):
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

        if option != 0:
            if not isinstance(option, int):
                print("You should to pass a number.")
                option = int(input(": "))

            loguru.logger.info("Populating database...")

            functions = [
                self.init_db,
                populate_admin,
                populate_home_contents,
                populate_posts,
                populate_projects,
                populate_socials,
                populate_tags
            ]

            functions[option]()


DBM = DBManager()
DBM.populate()
