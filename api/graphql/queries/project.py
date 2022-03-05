from graphene_sqlalchemy import SQLAlchemyObjectType

from api.db.models.Project import Project


class Project(SQLAlchemyObjectType):
    class Meta:
        model = Project