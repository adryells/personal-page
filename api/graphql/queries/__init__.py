import graphene

from api.graphql.queries.main import AllNameSpaces
from api.graphql.util import MountGraphQLObject


class Query(graphene.ObjectType,
            MountGraphQLObject(AllNameSpaces),
            ):
    pass
