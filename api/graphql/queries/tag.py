import graphene

from api.controllers.tagcontroller import TagController
from api.graphql.types import TagType
from api.graphql.util import WaverGraphQLResolveInfo


class TagQ(graphene.ObjectType):
    tags = graphene.List(TagType,
                         page=graphene.Argument(graphene.Int),
                         perpage=graphene.Argument(graphene.Int)
                         )
    tag = graphene.Field(TagType, tagid=graphene.Argument(graphene.Int))

    def resolve_tags(self, info: WaverGraphQLResolveInfo, page: int = None, perpage: int = None):
        return TagController(info.context.session).get_all_tags(page, perpage)

    def resolve_tag(self, info: WaverGraphQLResolveInfo, tagid: int):
        return TagController(info.context.session).get_tag_by_id(tagid)