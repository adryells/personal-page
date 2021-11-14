from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Boolean
# from sqlalchemy.orm import scoped_session, sessionmaker


class Config:
    Base = declarative_base()
    engine = create_engine("sqlite:///../YELLpersonalpage.db", echo=True, future=True,
                           connect_args={'check_same_thread': False})
    session = Session(engine, future=True)
    #session = scoped_session(sessionmaker(bind=engine))


class Post(Config.Base):
    __tablename__ = "posts"

    postid = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=False)
    media = Column(String)
    active = Column(Boolean, default=True)

    def __repr__(self):
        return f"Post(id={self.postid}, title={self.title}"


class Project(Config.Base):
    __tablename__ = "projects"

    projectid = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    shortdescription = Column(String, nullable=False)
    bigdescription = Column(String, default=shortdescription)
    link = Column(String, nullable=False)
    media = Column(String)
    published = Column(Boolean)
    active = Column(Boolean, default=True)

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


class Technology(Config.Base):
    __tablename__ = 'technologies'

    technologyid = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    link = Column(String, nullable=False)
    experience = Column(String, nullable=False)
    media = Column(String)
    situation = Column(String)
    active = Column(Boolean, default=True)

    def __repr__(self):
        return f"Technology(id={self.technologyid}, name={self.name}"
