from graphene_sqlalchemy import SQLAlchemyObjectType

from api.db.models.Tag import Tag


class Tag(SQLAlchemyObjectType):
    class Meta:
        model = Tag