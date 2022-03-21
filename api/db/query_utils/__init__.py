from typing import Type, Optional

from sqlalchemy.orm import Session, Query

from api.db import get_session, Base


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
