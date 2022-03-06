from sqlalchemy import Column, Integer, String, Boolean

from api.db import Base

# TODO: to implement token


class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    status = Column(Boolean, default=False)
    token = Column(Boolean)

    def __repr__(self):
        return f"Admin(id={self.id}, name={self.username}"