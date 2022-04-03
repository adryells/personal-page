from faker import Faker
from loguru import logger
from psycopg2.sql import SQL, Identifier
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, close_all_sessions
from starlette.testclient import TestClient
import pytest

from api.db import get_session, engine
from api.tests.conect_db_test import settings, execute_in_db_connection
from api.utils.create_database import DBManager
from main import app

DBM = DBManager()

""" TODO: Ao rodar um teste a database principal está tendo os dados apagados pq to passando o engine principal, ent devo criar um fake engine com o msm fluxo do main """
@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    db_url = settings.db_params()
    test_db_name = Faker().pystr()

    logger.info(f'Creating Database "{test_db_name}" for running tests...')

    execute_in_db_connection(
        SQL("CREATE DATABASE {}").format(Identifier(test_db_name)),
    )

    yield

    close_all_sessions()

    logger.info(f'Dropping Database "{test_db_name}".')

    execute_in_db_connection(
        SQL("DROP DATABASE {}").format(Identifier(test_db_name)),
    )


@pytest.fixture(scope="session", autouse=True)
def create_db_schema(create_test_database):
    DBM.init_db(engine)


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
