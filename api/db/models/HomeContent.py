from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from api.db.db import Base


class HomeContent(Base):
    __tablename__ = "homecontents"

    homecontentid = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    homecontenttype = Column(String, nullable=False)
    datecreated = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"HomeContent(id={self.homecontentid}, content={self.content}"