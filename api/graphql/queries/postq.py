import graphene

from api.db.models.Post import Post
from api.graphql.types import PostType
from api.graphql.util import WaverGraphQLResolveInfo


class PostQ(graphene.ObjectType):
    posts = graphene.List(PostType,
                          page=graphene.Argument(graphene.Int, default_value=1),
                          perpage=graphene.Argument(graphene.Int, default_value=50)
                          )
    post = graphene.Field(PostType, postid=graphene.Argument(type_=graphene.Int))

    def resolve_posts(self, info: WaverGraphQLResolveInfo, page: int, perpage: int):
        return info.context.session.query(Post).limit(perpage).offset((page - 1) * perpage).all()

    def resolve_post(self, info: WaverGraphQLResolveInfo, postid: int):
        return info.context.session.query(Post).filter(Post.postid == postid).one_or_none()
