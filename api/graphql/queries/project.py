import graphene

from api.db.models.Project import Project
from api.graphql.types import ProjectType
from api.graphql.util import WaverGraphQLResolveInfo


class ProjectQ(graphene.ObjectType):
    projects = graphene.List(ProjectType,
                             page=graphene.Argument(graphene.Int, default_value=1),
                             perpage=graphene.Argument(graphene.Int, default_value=50),
                             )
    project = graphene.Field(ProjectType, projectid=graphene.Argument(type_=graphene.Int))

    def resolve_projects(self, info: WaverGraphQLResolveInfo, page: int, perpage: int):
        return info.context.session.query(Project).limit(perpage).offset((page-1) * perpage).all()

    def resolve_project(self, info: WaverGraphQLResolveInfo, projectid: int):
        return info.context.session.query(Project).filter(Project.projectid == projectid).one_or_none()