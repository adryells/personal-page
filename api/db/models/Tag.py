from sqlalchemy import Table, ForeignKey, Column, Integer, String, Boolean

from api.db import Base

tag_posts = Table('tagposts', Base.metadata,
    Column('post_id', ForeignKey('posts.id')),
    Column('tag_id', ForeignKey('tags.id'))
)

tag_projects = Table('projecttags', Base.metadata,
    Column('project_id', ForeignKey('projects.id')),
    Column('tag_id', ForeignKey('tags.id'))
)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    portuguese_name = Column(String, nullable=False, default="tag_name")
    english_name = Column(String, nullable=True, default="tag_name")
    active = Column(Boolean, default=True)

    def __repr__(self):
        return f"Tag(id={self.id}, name={self.portuguese_name}"