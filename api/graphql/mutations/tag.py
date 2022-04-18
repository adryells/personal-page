import graphene

from api.controllers.tagcontroller import TagController
from api.graphql.types import TagType
from api.graphql.util import WaverGraphQLResolveInfo


class InputTag(graphene.InputObjectType):
    portuguese_name = graphene.String(required=True)
    english_name = graphene.String()
    active = graphene.Boolean(default=True)


class AddOrUpdateTag(graphene.Mutation):
    class Arguments:
        data = InputTag()

    tag = graphene.Field(TagType)

    def mutate(self, info: WaverGraphQLResolveInfo, data: InputTag):
        tag = TagController(info.context.session).add_or_update_tag(
            portuguese_name=data.portuguese_name,
            english_name=data.english_name,
            active=data.active
        )

        return AddOrUpdateTag(tag=tag)


class RemoveTag(graphene.Mutation):
    class Arguments:
        post_id = graphene.Int()
        project_id = graphene.Int()
        tag_id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info: WaverGraphQLResolveInfo, post_id: int, project_id: int, tag_id: int):
        success = TagController(info.context.session).remove_tag_from(post_id, project_id, tag_id)

        return RemoveTag(success=success)
