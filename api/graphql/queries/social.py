import graphene

from api.controllers.socialcontroller import SocialController
from api.graphql.types import SocialType
from api.graphql.util import WaverGraphQLResolveInfo


class SocialQ(graphene.ObjectType):
    socials = graphene.List(SocialType,
                            page=graphene.Argument(graphene.Int),
                            perpage=graphene.Argument(graphene.Int),
                            )
    social = graphene.Field(SocialType, social_id=graphene.Argument(graphene.Int))

    def resolve_socials(self, info: WaverGraphQLResolveInfo, page: int = None, perpage: int = None):
        return SocialController(info.context.session).get_all_socials(page, perpage)

    def resolve_social(self, info: WaverGraphQLResolveInfo, social_id: int):
        return SocialController(info.context.session).get_social_by_id(social_id)
