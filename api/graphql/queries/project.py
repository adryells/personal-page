from typing import List

import graphene

from api.controllers.projectcontroller import ProjectController
from api.graphql.queries.enums import BasicOrderEnum
from api.graphql.types import ProjectType
from api.graphql.util import WaverGraphQLResolveInfo


class ProjectQ(graphene.ObjectType):
    projects = graphene.List(ProjectType,
                             status=graphene.Argument(graphene.Boolean),
                             tags=graphene.Argument(graphene.List(graphene.String)),
                             page=graphene.Argument(graphene.Int),
                             perpage=graphene.Argument(graphene.Int),
                             order=graphene.Argument(BasicOrderEnum)
                             )
    project = graphene.Field(ProjectType, project_id=graphene.Argument(type_=graphene.Int))

    def resolve_projects(self, info: WaverGraphQLResolveInfo, page: int, perpage: int, status: bool, tags: List[str],
                         order: BasicOrderEnum):
        return ProjectController(info.context.session).get_all_projects(page, perpage, status, tags, order.value)

    def resolve_project(self, info: WaverGraphQLResolveInfo, project_id: int):
        return ProjectController(info.context.session).get_project_by_id(project_id)
