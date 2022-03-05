from graphene_sqlalchemy import SQLAlchemyObjectType

from api.db.models.Admin import Admin


class Admin(SQLAlchemyObjectType):
    class Meta:
        model = Admin
