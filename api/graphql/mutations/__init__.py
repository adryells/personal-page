import graphene

from api.graphql.mutations.social import UpdateSocial
from api.graphql.util import MountGraphQLObject


class Mutation(graphene.ObjectType,
               MountGraphQLObject(UpdateSocial)):
    pass