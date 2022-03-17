import graphene

from api.graphql.mutations.project import UpdateProject, AddProject
from api.graphql.mutations.social import UpdateSocial
from api.graphql.util import MountGraphQLObject


class Mutation(graphene.ObjectType,
               MountGraphQLObject(UpdateSocial),
               MountGraphQLObject(UpdateProject),
               MountGraphQLObject(AddProject),
               ):
    pass