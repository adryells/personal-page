from sqlalchemy import Column, Integer, String, Boolean

from api.db import Base


class Social(Base):
    __tablename__ = "socials"

    socialid = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    link = Column(String, nullable=False)
    media = Column(String)
    active = Column(Boolean, default=True)

    def __repr__(self):
        return f"Social(id={self.socialid}, name={self.name}"
