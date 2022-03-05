from api.db.models.Project import Project
from api.graphql.util import SQLAlchemyObjectArueType


class ProjectType(SQLAlchemyObjectArueType):
    class Meta:
        model = Project
