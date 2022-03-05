import graphene

from api.db.models.Project import Project
from api.graphql.types import ProjectType
from api.graphql.util import WaverGraphQLResolveInfo


class ProjectQ(graphene.ObjectType):
    projects = graphene.List(ProjectType)
    project = graphene.Field(ProjectType, projectid=graphene.Argument(type_=graphene.Int))

    def resolve_projects(self, info: WaverGraphQLResolveInfo):
        return info.context.session.query(Project).all()

    def resolve_project(self, info: WaverGraphQLResolveInfo, projectid: int):
        return info.context.session.query(Project).filter(Project.projectid == projectid).one_or_none()