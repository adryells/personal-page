from api.db.db import Base, engine
from api.db.models import (
    Admin,
    HomeContent,
    Tag,
    Post,
    Social,
    Project
)

Base.metadata.create_all(engine)
