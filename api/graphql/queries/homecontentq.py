import graphene

from api.controllers.homecontentcontroller import HomeContentController
from api.db.models.HomeContent import HomeContent
from api.graphql.types import HomeContentType
from api.graphql.util import WaverGraphQLResolveInfo


class HomeContentQ(graphene.ObjectType):
    home_contents = graphene.List(HomeContentType,
                                  status=graphene.Argument(graphene.Boolean),
                                  page=graphene.Argument(graphene.Int),
                                  perpage=graphene.Argument(graphene.Int),
                                  )

    def resolve_home_contents(self, info: WaverGraphQLResolveInfo,
                              status: bool = None, page: int = None, perpage: int = None):

        return HomeContentController(info.context.session).get_all_home_contents(status, page, perpage)
