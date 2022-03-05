import graphene

from api.db.models.Project import Project
from api.graphql.types.project import ProjectType
from api.graphql.util import WaverGraphQLResolveInfo


class ProjectQ(graphene.ObjectType):
    projects = graphene.List(ProjectType)

    def resolve_projects(self, info: WaverGraphQLResolveInfo):
        return info.context.session.query(Project).all()