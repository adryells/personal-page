import graphene

from api.db.models.Post import Post
from api.graphql.types.post import PostType
from api.graphql.util import WaverGraphQLResolveInfo


class Post(graphene.ObjectType):
    posts = graphene.List(PostType)

    def resolve_posts(self, info: WaverGraphQLResolveInfo):
        return info.context.session.query(Post).all()
