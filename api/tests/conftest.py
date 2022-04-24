from faker import Faker
from loguru import logger
from psycopg2.sql import SQL, Identifier
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, close_all_sessions
from starlette.testclient import TestClient
import pytest

from api.db import get_session, build_engine
from api.tests.conect_db_test import execute_in_db_connection, DatabaseParameters
from api.utils.create_database import DBManager
from api.utils.settings import Settings
from main import app

DBM = DBManager()
settings = Settings()
fake_string = Faker().pystr()
engine = build_engine(settings.TEST_DB_URL + fake_string)


@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    database_parameters = DatabaseParameters.from_db_url(settings.TEST_DB_URL + fake_string)

    logger.info(f'Creating Database "{database_parameters.db_name}" for running tests...')

    execute_in_db_connection(
        database_parameters,
        SQL("CREATE DATABASE {}").format(Identifier(database_parameters.db_name))
    )

    yield

    close_all_sessions()

    logger.info(f'Dropping Database "{database_parameters.db_name}".')

    execute_in_db_connection(
        database_parameters,
        SQL("DROP DATABASE {}").format(Identifier(database_parameters.db_name)),
    )


@pytest.fixture(scope="session", autouse=True)
def create_db_schema(create_test_database):
    DBM.create_all_tables(engine_=engine, populate=True)


@pytest.fixture(scope='session', autouse=True)
def get_database_connection(create_db_schema) -> Engine:
    yield engine

    engine.dispose()


@pytest.fixture
def session() -> Session:
    yield from get_session()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
