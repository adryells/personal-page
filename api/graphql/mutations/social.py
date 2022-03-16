import graphene

from api.controllers.socialcontroller import SocialController
from api.graphql.types import SocialType
from api.graphql.util import WaverGraphQLResolveInfo


class InputUpdateSocial(graphene.InputObjectType):
    social_id = graphene.Int()
    name = graphene.String()
    link = graphene.String()
    media = graphene.String()
    active = graphene.Boolean()


class UpdateSocial(graphene.Mutation):
    class Arguments:
        data = InputUpdateSocial()

    success = graphene.Boolean()
    social = graphene.Field(SocialType)

    def mutate(self, info: WaverGraphQLResolveInfo, data: InputUpdateSocial):
        social = SocialController(info.context.session)\
            .update_social(
                data.social_id,
                data.name,
                data.active,
                data.link,
                data.media
        )

        return UpdateSocial(success=True, social=social)


