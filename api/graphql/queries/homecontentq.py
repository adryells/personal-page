import graphene

from api.db.models.HomeContent import HomeContent
from api.graphql.types import HomeContentType
from api.graphql.util import WaverGraphQLResolveInfo


class HomeContentQ(graphene.ObjectType):
    home_contents = graphene.List(HomeContentType)

    def resolve_home_contents(self, info: WaverGraphQLResolveInfo):
        return info.context.session.query(HomeContent).all()
