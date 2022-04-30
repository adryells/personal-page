from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class HomeContentType(Base):
    __tablename__ = "homecontenttypes"
    id = Column(Integer, primary_key=True)
    slug = Column(String, nullable=False)


class HomeContent(Base):
    __tablename__ = "homecontents"

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    homecontenttype_id = Column(Integer, ForeignKey("homecontenttypes.id"))
    homecontenttype = relationship(HomeContentType)
    active = Column(Boolean, default=True)
    datecreated = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"HomeContent(id={self.id}"
