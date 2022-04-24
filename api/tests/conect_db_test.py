import re

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from pydantic import BaseModel


class DatabaseParameters(BaseModel):
    schema_name: str = "postgresql"
    user: str
    password: str
    host: str
    port: int
    db_name: str

    @classmethod
    def from_db_url(cls, db_url: str) -> 'DatabaseParameters':
        schema, _, user, password, host, port, db_name = re.search(
            r"(.*?)\+(.*?)\:\/\/(.*?)\:(.*?)\@(.*)\:(.*)\/(.*)", db_url).groups()

        return cls(schema_name=schema,
                   user=user,
                   password=password,
                   host=host,
                   port=port,
                   db_name=db_name)


def execute_in_db_connection(db: DatabaseParameters, command: str):
    db_connection = psycopg2.connect(
        user=db.user,
        password=db.password,
        host=db.host,
        port=db.port,
        dbname="postgres"
    )

    db_connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = db_connection.cursor()

    cursor.execute(command)

    cursor.close()

    db_connection.close()
