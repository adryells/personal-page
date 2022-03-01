import datetime

from sqlalchemy import Column, String, Integer, Date, Boolean
from sqlalchemy.orm import relationship

from api.db.db import Base
from api.db.models.Tag import tag_posts


class Post(Base):
    __tablename__ = "posts"

    postid = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    englishtitle = Column(String, default="title")
    description = Column(String, nullable=False)
    descriptionenglish = Column(String, default="description")
    content = Column(String, nullable=False)
    contentenglish = Column(String, default="content")
    media = Column(String)
    active = Column(Boolean, default=True)
    datecreated = Column(Date, default=datetime.date.today())
    tags = relationship("Tag", secondary=tag_posts)


    def __repr__(self):
        return f"Post(id={self.postid}, title={self.title}"










