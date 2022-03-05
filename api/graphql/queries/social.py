from graphene_sqlalchemy import SQLAlchemyObjectType

from api.db.models.Social import Social


class Social(SQLAlchemyObjectType):
    class Meta:
        model = Social