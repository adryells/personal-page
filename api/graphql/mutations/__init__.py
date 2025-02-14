import graphene

from api.graphql.mutations.home import AddHomeContent, UpdateHomeContent
from api.graphql.mutations.post import AddPost, UpdatePost
from api.graphql.mutations.project import UpdateProject, AddProject
from api.graphql.mutations.social import UpdateSocial, AddSocial
from api.graphql.mutations.tag import AddOrUpdateTag, RemoveTag
from api.graphql.util import MountGraphQLObject


# TODO: Adicionar validações para cada campo

class Mutation(graphene.ObjectType,
               MountGraphQLObject(UpdateSocial),
               MountGraphQLObject(UpdateProject),
               MountGraphQLObject(AddProject),
               MountGraphQLObject(AddSocial),
               MountGraphQLObject(AddHomeContent),
               MountGraphQLObject(UpdateHomeContent),
               MountGraphQLObject(AddOrUpdateTag),
               MountGraphQLObject(AddPost),
               MountGraphQLObject(UpdatePost),
               MountGraphQLObject(RemoveTag),
               ):
    pass
