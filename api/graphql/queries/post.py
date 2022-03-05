from graphene_sqlalchemy import SQLAlchemyObjectType

from api.db.models.Post import Post


class Post(SQLAlchemyObjectType):
    class Meta:
        model = Post