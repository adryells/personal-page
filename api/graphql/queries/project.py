import graphene

from api.controllers.projectcontroller import ProjectController
from api.graphql.types import ProjectType
from api.graphql.util import WaverGraphQLResolveInfo


class ProjectQ(graphene.ObjectType):
    projects = graphene.List(ProjectType,
                             status=graphene.Argument(graphene.Boolean),
                             page=graphene.Argument(graphene.Int),
                             perpage=graphene.Argument(graphene.Int),
                             )
    project = graphene.Field(ProjectType, project_id=graphene.Argument(type_=graphene.Int))

    def resolve_projects(self, info: WaverGraphQLResolveInfo, page: int, perpage: int, status: bool):
        return ProjectController(info.context.session).get_all_projects(page, perpage, status)

    def resolve_project(self, info: WaverGraphQLResolveInfo, project_id: int):
        return ProjectController(info.context.session).get_project_by_id(project_id)