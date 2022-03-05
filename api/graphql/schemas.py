import graphene

from api.graphql.queries.admin import Admin
from api.graphql.queries.homecontent import HomeContent
from api.graphql.queries.post import Post
from api.graphql.queries.project import Project
from api.graphql.queries.social import Social
from api.graphql.queries.tag import Tag
from api.graphql.templates.config import custom_dark_make_graphiql_handler
from starlette_graphene3 import GraphQLApp

from api.graphql.util import MountGraphQLObject


class Query(graphene.ObjectType,
            MountGraphQLObject(Admin),
            MountGraphQLObject(HomeContent),
            MountGraphQLObject(Post),
            MountGraphQLObject(Project),
            MountGraphQLObject(Social),
            MountGraphQLObject(Tag),
            ):

    pass


class Mutation(graphene.ObjectType):
    ...


graphql_schema = graphene.Schema(query=Query)

graphql_app = GraphQLApp(schema=graphql_schema, on_get=custom_dark_make_graphiql_handler())
