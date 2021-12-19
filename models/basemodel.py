from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Boolean, MetaData, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
import datetime


class Config:
    Base = declarative_base()
    engine = create_engine("sqlite:///database.db", echo=True, future=True,
                           connect_args={'check_same_thread': False})
    session = Session(engine, future=True)
    metadata = MetaData(engine)

tag_posts = Table('tagposts', Config.Base.metadata,
    Column('post_id', ForeignKey('posts.postid')),
    Column('tag_id', ForeignKey('tags.tagid'))
)

tag_projects = Table('projecttags', Config.Base.metadata,
    Column('project_id', ForeignKey('projects.projectid')),
    Column('tag_id', ForeignKey('tags.tagid'))
)

class Post(Config.Base):
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


class Project(Config.Base):
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


class Social(Config.Base):
    __tablename__ = "socials"

    socialid = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    link = Column(String, nullable=False)
    media = Column(String)
    active = Column(Boolean, default=True)

    def __repr__(self):
        return f"Social(id={self.socialid}, name={self.name}"

class Tag(Config.Base):
    __tablename__ = "tags"

    tagid = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default="tag_name")
    active = Column(Boolean, default=True)

    def __repr__(self):
        return f"Tag(id={self.tagid}, name={self.name}"