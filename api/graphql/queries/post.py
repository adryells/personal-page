from typing import List

import graphene

from api.controllers.postcontroller import PostController
from api.graphql.queries.enums import BasicOrderEnum
from api.graphql.types import PostType
from api.graphql.util import WaverGraphQLResolveInfo


class PostQ(graphene.ObjectType):
    posts = graphene.List(PostType,
                          tags=graphene.Argument(graphene.List(graphene.String)),
                          status=graphene.Argument(graphene.Boolean),
                          page=graphene.Argument(graphene.Int),
                          perpage=graphene.Argument(graphene.Int),
                          order=graphene.Argument(BasicOrderEnum)
                          )
    post = graphene.Field(PostType, post_id=graphene.Argument(type_=graphene.Int))

    def resolve_posts(self, info: WaverGraphQLResolveInfo, page: int, perpage: int, status: bool, tags: List[str],
                      order: BasicOrderEnum):
        return PostController(info.context.session).get_all_posts(page, perpage, status, tags, order)

    def resolve_post(self, info: WaverGraphQLResolveInfo, post_id: int):
        return PostController(info.context.session).get_post_by_id(post_id)
