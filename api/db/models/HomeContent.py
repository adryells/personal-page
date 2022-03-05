from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean

from api.db import Base


class HomeContent(Base):
    __tablename__ = "homecontents"

    homecontentid = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    homecontenttype = Column(String, nullable=False)
    active = Column(Boolean, default=True)
    datecreated = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"HomeContent(id={self.homecontentid}"