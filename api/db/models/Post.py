import datetime

from sqlalchemy import Column, String, Integer, Date, Boolean
from sqlalchemy.orm import relationship

from api.db import Base
from api.db.models.Tag import tag_posts

# TODO: implement media


class Post(Base):
    __tablename__ = "posts"

    postid = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    english_title = Column(String, default="title")
    description = Column(String, nullable=False)
    english_description = Column(String, default="description")
    content = Column(String, nullable=False)
    english_content = Column(String, default="content")
    media = Column(String)
    active = Column(Boolean, default=True)
    datecreated = Column(Date, default=datetime.date.today())
    tags = relationship("Tag", secondary=tag_posts)

    def __repr__(self):
        return f"Post(id={self.postid}, title={self.title}"










