import datetime
from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship

from api.db import Base
from api.db.models.Tag import tag_projects


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    english_title = Column(String, default="title")
    description = Column(String, nullable=False)
    english_description = Column(String, default="shortdescription")
    bigdescription = Column(String, default="big_description")
    english_bigdescription = Column(String, default="bigdescription")
    link = Column(String, nullable=False)
    media = Column(String)
    active = Column(Boolean, default=True)
    datecreated = Column(Date, default=datetime.date.today())
    tags = relationship("Tag", secondary=tag_projects)

    def __repr__(self):
        return f"Project(id={self.id}, title={self.title}"

