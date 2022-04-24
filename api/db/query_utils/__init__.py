import random

from sqlalchemy import func
from sqlalchemy.orm import Session, Query

from api.db import get_session


class DbBaseUtils:
    def __init__(self, session: Session = next(get_session())):
        self.session = session

    def get_object_by_id(self, model_class, object_id: int):
        object_db = self.session.query(model_class) \
            .filter(model_class.id == object_id) \
            .one_or_none()

        return object_db

    def get_all_objects_query(self, model_class) -> Query:
        query = self.session.query(model_class)

        return query

    def paginate_query(self, query: Query, page: int, perpage: int) -> Query:
        query = query.limit(perpage).offset((page - 1) * perpage)

        return query

    def count_query(self, query: Query) -> int:
        count = query.session.execute(query.statement.with_only_columns([func.count()])).scalar()

        return count

    def get_random_register_from_table(self, table):
        random_register = random.randrange(0, self.session.query(table).count())

        return self.session.query(table)[random_register]
