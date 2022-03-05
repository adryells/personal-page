import graphene

from api.db.models.Post import Post
from api.graphql.types import PostType
from api.graphql.util import WaverGraphQLResolveInfo


class PostQ(graphene.ObjectType):
    posts = graphene.List(PostType)

    def resolve_posts(self, info: WaverGraphQLResolveInfo):
        return info.context.session.query(Post).all()
