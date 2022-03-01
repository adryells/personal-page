from sqlalchemy import Column, Integer, String

from api.db.db import Base


class HomeContent(Base):
    __tablename__ = "homecontents"

    homecontentid = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    theme = Column(String, nullable=False)

    def __repr__(self):
        return f"HomeContent(id={self.homecontentid}, content={self.content}"