import os


class Settings:

    BASE_DIRECTORY = os.path.join(os.path.dirname(__file__))
    TEST_DB_URL = 'postgresql+psycopg2://postgres:12345678@127.0.0.1:5433/'
    DB_URL = 'postgresql+psycopg2://postgres:12345678@127.0.0.1:5433/wavers'

    def db_params(self,
                  schema_name: str = "postgresql",
                  user: str = "",
                  password: str = "",
                  host: str = "",
                  port: str = "",
                  db_name: str = ""
                  ):

        db_data = {
            "schema_name": schema_name,
            "user": user,
            "password": password,
            "host": host,
            "port": port,
            "db_name": db_name
        }

        return db_data
