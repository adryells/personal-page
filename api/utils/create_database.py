
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

    def create_all_tables(self, engine_: Engine, populate: bool = False):
        loguru.logger.info("Creating database...")
        Base.metadata.create_all(engine_ or engine)

        if populate:
            self.populate()

    def init_db(self, engine_: Engine):
        self.drop_all_tables(engine_ or engine)
        self.create_all_tables(engine_ or engine)

    def populate(self):

        loguru.logger.info("Populating database...")

        functions = [
            populate_tags,
            populate_admin,
            populate_home_contents,
            populate_posts,
            populate_projects,
            populate_socials
        ]

        [function() for function in functions]


DBM = DBManager()
DBM.populate()
