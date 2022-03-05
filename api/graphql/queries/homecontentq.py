import graphene

from api.db.models.HomeContent import HomeContent
from api.graphql.types import HomeContentType
from api.graphql.util import WaverGraphQLResolveInfo


class HomeContentQ(graphene.ObjectType):
    home_contents = graphene.List(HomeContentType, active=graphene.Argument(graphene.Boolean, default_value=True))

    def resolve_home_contents(self, info: WaverGraphQLResolveInfo, active: bool):
        return info.context.session.query(HomeContent).filter(HomeContent.active == active).all()
