from sqlalchemy import Table, ForeignKey, Column, Integer, String, Boolean

from api.db.db import Base

tag_posts = Table('tagposts', Base.metadata,
    Column('post_id', ForeignKey('posts.postid')),
    Column('tag_id', ForeignKey('tags.tagid'))
)

tag_projects = Table('projecttags', Base.metadata,
    Column('project_id', ForeignKey('projects.projectid')),
    Column('tag_id', ForeignKey('tags.tagid'))
)


class Tag(Base):
    __tablename__ = "tags"

    tagid = Column(Integer, primary_key=True)
    portuguese_name = Column(String, nullable=False, default="tag_name")
    english_name = Column(String, nullable=True, default="tag_name")
    active = Column(Boolean, default=True)

    def __repr__(self):
        return f"Tag(id={self.tagid}, name={self.portuguese_name}"