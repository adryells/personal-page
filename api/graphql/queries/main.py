import graphene

from api.graphql.queries.adminq import AdminQ
from api.graphql.queries.homecontentq import HomeContentQ
from api.graphql.queries.postq import PostQ
from api.graphql.queries.project import ProjectQ
from api.graphql.queries.socialq import SocialQ
from api.graphql.queries.tag import TagQ

# TODO: Fix: status=false not working
# TODO: Reuse: When changed modelid to id, to use SQLALchemyObjectArueType in queries


class AllNameSpaces(graphene.ObjectType):
    post = graphene.Field(PostQ, resolver=lambda _, __: _)
    project = graphene.Field(ProjectQ, resolver=lambda _, __: _)
    social = graphene.Field(SocialQ, resolver=lambda _, __: _)
    tag = graphene.Field(TagQ, resolver=lambda _, __: _)
    admin = graphene.Field(AdminQ, resolver=lambda _, __: _)
    home_content = graphene.Field(HomeContentQ, resolver=lambda _, __: _)