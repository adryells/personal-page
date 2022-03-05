import graphene

from api.db.models.Social import Social
from api.graphql.types import SocialType
from api.graphql.util import WaverGraphQLResolveInfo


class SocialQ(graphene.ObjectType):
    socials = graphene.List(SocialType)
    social = graphene.Field(SocialType, socialid=graphene.Argument(graphene.Int))

    def resolve_socials(self, info: WaverGraphQLResolveInfo):
        return info.context.session.query(Social).all()

    def resolve_social(self, info: WaverGraphQLResolveInfo, socialid: int):
        return info.context.session.query(Social).filter(Social.socialid == socialid).one_or_none()
