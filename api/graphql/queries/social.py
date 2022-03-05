import graphene

from api.db.models.Social import Social
from api.graphql.types.social import SocialType
from api.graphql.util import WaverGraphQLResolveInfo


class Social(graphene.ObjectType):
    socials = graphene.List(SocialType)

    def resolve_socials(self, info: WaverGraphQLResolveInfo):
        return info.context.session.query(Social).all()