import graphene

from api.controllers.socialcontroller import SocialController
from api.graphql.types import SocialType
from api.graphql.util import WaverGraphQLResolveInfo


class InputUpdateSocial(graphene.InputObjectType):
    social_id = graphene.Int(required=True)
    name = graphene.String()
    link = graphene.String()
    media = graphene.String()
    active = graphene.Boolean()


class InputAddSocial(graphene.InputObjectType):
    name = graphene.String(required=True)
    link = graphene.String(required=True)
    media = graphene.String(required=True)
    active = graphene.Boolean(default_value=True)


class UpdateSocial(graphene.Mutation):
    class Arguments:
        data = InputUpdateSocial()

    success = graphene.Boolean()
    social = graphene.Field(SocialType)

    def mutate(self, info: WaverGraphQLResolveInfo, data: InputUpdateSocial):
        social = SocialController(info.context.session) \
            .update_social(
            data.social_id,
            data.name,
            data.active,
            data.link,
            data.media
        )

        return UpdateSocial(success=True, social=social)


class AddSocial(graphene.Mutation):
    class Arguments:
        data = InputAddSocial()

    social = graphene.Field(SocialType)

    def mutate(self, info: WaverGraphQLResolveInfo, data: InputAddSocial):
        social = SocialController(info.context.session).add_social(
            name=data.name,
            link=data.link,
            media=data.media,
            active=data.active
        )

        return AddSocial(social=social)
