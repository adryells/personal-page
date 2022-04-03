import os


class GeneralSettings:

    BASE_DIRECTORY = os.path.join(os.path.dirname(__file__))
    DB_URL = 'postgresql+psycopg2://postgres:12345678@127.0.0.1:5433/wavers'

    def db_params(self,
                  schema_name: str = "postgresql",
                  user: str = "postgres",
                  password: str = "12345678",
                  host: str = "127.0.0.1",
                  port: str = "5433",
                  db_name: str = "wavers"
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


class Development(GeneralSettings):
    ...


class Production(GeneralSettings):
    ...
