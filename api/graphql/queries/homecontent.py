import graphene

from api.db.models.HomeContent import HomeContent
from api.graphql.types.homecontent import HomeContentType
from api.graphql.util import WaverGraphQLResolveInfo




class HomeContent(graphene.ObjectType):
    home_contents = graphene.List(HomeContentType)

    def resolve_home_contents(self, info: WaverGraphQLResolveInfo):
        return info.context.session.query(HomeContent).all()
