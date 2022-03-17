from datetime import datetime
import graphene

from api.controllers.postcontroller import PostController
from api.graphql.types import PostType
from api.graphql.util import WaverGraphQLResolveInfo


class InputAddPost(graphene.InputObjectType):
    title = graphene.String(required=True)
    english_title = graphene.String()
    description = graphene.String(required=True)
    english_description = graphene.String()
    content = graphene.String(required=True)
    english_content = graphene.String()
    media = graphene.String()
    active = graphene.Boolean(default_value=True)
    datecreated = graphene.DateTime(default_value=datetime.now())
    tags = graphene.List(graphene.String)


class InputUpdatePost(graphene.InputObjectType):
    post_id = graphene.Int(required=True)
    title = graphene.String()
    english_title = graphene.String()
    description = graphene.String()
    english_description = graphene.String()
    content = graphene.String()
    english_content = graphene.String()
    media = graphene.String()
    active = graphene.Boolean()
    datecreated = graphene.DateTime()
    tags = graphene.List(graphene.String)


class UpdatePost(graphene.Mutation):
    class Arguments:
        data = InputUpdatePost()

    post = graphene.Field(PostType)

    def mutate(self, info: WaverGraphQLResolveInfo, data: InputUpdatePost):
        post = PostController(info.context.session).update_post(
            data.post_id,
            data.title,
            data.english_title,
            data.description,
            data.english_description,
            data.content,
            data.english_content,
            data.media,
            data.active,
            data.datecreated,
            data.tags
        )

        return UpdatePost(post=post)


class AddPost(graphene.Mutation):
    class Arguments:
        data = InputAddPost()

    post = graphene.Field(PostType)

    def mutate(self, info: WaverGraphQLResolveInfo, data: InputAddPost):
        post = PostController(info.context.session).add_post(
            data.title,
            data.english_title,
            data.description,
            data.english_description,
            data.content,
            data.english_content,
            data.media,
            data.active,
            data.datecreated,
            data.tags
        )

        return AddPost(post=post)