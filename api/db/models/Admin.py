import hashlib
import os
import uuid

from sqlalchemy import Column, Integer, String, Boolean

from api.db import Base


class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    salt = Column(String, nullable=False)
    status = Column(Boolean, default=False)
    token = Column(String, nullable=False)

    def __repr__(self):
        return f"Admin(id={self.id}, username={self.username}"

    def generate_token(self):
        token = hashlib.sha256(str(uuid.uuid4()).encode("utf8")).hexdigest()
        self.token = token
        return self.token

    def generate_salt(self) -> bytes:
        self.salt = os.urandom(32)
        return self.salt

    def generate_password(self, password: str, salt: bytes) -> bytes:
        self.password = hashlib.pbkdf2_hmac(
            hash_name='sha256',
            password=password.encode('utf-8'),
            salt=salt,
            iterations=8600,
            dklen=128
        )
        return self.password
