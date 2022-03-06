from sqlalchemy import Column, Integer, String, Boolean

from api.db import Base


class Social(Base):
    __tablename__ = "socials"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    link = Column(String, nullable=False)
    media = Column(String)
    active = Column(Boolean, default=True)

    def __repr__(self):
        return f"Social(id={self.id}, name={self.name}"
