import graphene
from starlette.background import BackgroundTasks
from starlette.requests import Request

from api.db import get_session
from api.graphql.mutations import Mutation
from api.graphql.queries import Query
from api.graphql.templates.config import custom_dark_make_graphiql_handler
from starlette_graphene3 import GraphQLApp

from api.graphql.util import GraphQLAppContext


def make_context(request: Request,
                 session=next(get_session())):
    return GraphQLAppContext(
        request=request,
        session=session,
        authorization=request.headers.get("Authorization"),
        background=BackgroundTasks(),
    )


graphql_schema = graphene.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLApp(
    schema=graphql_schema,
    context_value=make_context,
    on_get=custom_dark_make_graphiql_handler()
)
