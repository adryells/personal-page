from sqlalchemy.orm import Session

from api.db import get_session


class BaseController:
    def __init__(self, db_session: Session = get_session()):
        self.session = db_session
