import graphene
from starlette_graphene3 import GraphQLApp

from api.graphql.templates.config import custom_dark_make_graphiql_handler


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "hello, Adryell!"


class Mutation(graphene.ObjectType):
    ...


graphql_schema = graphene.Schema(query=Query)

graphql_app = GraphQLApp(schema=graphql_schema, on_get=custom_dark_make_graphiql_handler())
