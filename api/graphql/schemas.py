import graphene
from starlette.background import BackgroundTasks
from starlette.requests import Request

from api.db.db import get_session
from api.graphql.queries.adminq import AdminQ
from api.graphql.queries.homecontentq import HomeContentQ
from api.graphql.queries.postq import PostQ
from api.graphql.queries.project import Project, ProjectQ
from api.graphql.queries.socialq import SocialQ
from api.graphql.queries.tag import TagQ
from api.graphql.templates.config import custom_dark_make_graphiql_handler
from starlette_graphene3 import GraphQLApp

from api.graphql.util import MountGraphQLObject, GraphQLAppContext


class Query(graphene.ObjectType,
            MountGraphQLObject(AdminQ),
            MountGraphQLObject(HomeContentQ),
            MountGraphQLObject(PostQ),
            MountGraphQLObject(ProjectQ),
            MountGraphQLObject(SocialQ),
            MountGraphQLObject(TagQ),
            ):

    pass


class Mutation(graphene.ObjectType):
    ...


def make_context(request: Request,
                 session=next(get_session())):
    return GraphQLAppContext(
        request=request,
        session=session,
        authorization=request.headers.get("Authorization"),
        background=BackgroundTasks(),
    )


graphql_schema = graphene.Schema(query=Query)

graphql_app = GraphQLApp(
    schema=graphql_schema,
    context_value=make_context,
    on_get=custom_dark_make_graphiql_handler()
)
