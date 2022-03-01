import datetime
from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship

from api.db.db import Base
from api.db.models.Tag import tag_projects


class Project(Base):
    __tablename__ = "projects"

    projectid = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    englishtitle = Column(String, default="title")
    shortdescription = Column(String, nullable=False)
    shortdescriptionenglish = Column(String, default="shortdescription")
    bigdescription = Column(String, default=shortdescription)
    bigdescriptionenglish = Column(String, default="bigdescription")
    link = Column(String, nullable=False)
    media = Column(String)
    active = Column(Boolean, default=True)
    datecreated = Column(Date, default=datetime.date.today())
    tags = relationship("Tag", secondary=tag_projects)

    def __repr__(self):
        return f"Project(id={self.projectid}, title={self.title}"

