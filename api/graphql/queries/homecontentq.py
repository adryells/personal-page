import graphene

from api.db.models.HomeContent import HomeContent
from api.graphql.types import HomeContentType
from api.graphql.util import WaverGraphQLResolveInfo


class HomeContentQ(graphene.ObjectType):
    home_contents = graphene.List(HomeContentType,
                                  active=graphene.Argument(graphene.Boolean, default_value=True),
                                  page=graphene.Argument(graphene.Int, default_value=1),
                                  perpage=graphene.Argument(graphene.Int, default_value=50),
                                  )

    def resolve_home_contents(self, info: WaverGraphQLResolveInfo, active: bool, page: int, perpage: int):
        return info.context.session.query(HomeContent)\
            .filter(HomeContent.active == active)\
            .limit(perpage).offset((page - 1) * perpage).all()
