import psycopg2
from faker import Faker
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from api.utils.settings import GeneralSettings

settings = GeneralSettings()
test_db_name = Faker().pystr()
db_url = settings.db_params(db_name=test_db_name)


def execute_in_db_connection(command: str = ""):
    db_connection = psycopg2.connect(
        user=db_url["user"],
        password=db_url["password"],
        host=db_url["host"],
        port=db_url["port"],
        dbname="postgres"
    )

    db_connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = db_connection.cursor()

    cursor.execute(command)

    cursor.close()

    db_connection.close()

