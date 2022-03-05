from graphene_sqlalchemy import SQLAlchemyObjectType

from api.db.models.HomeContent import HomeContent


class HomeContent(SQLAlchemyObjectType):
    class Meta:
        model = HomeContent