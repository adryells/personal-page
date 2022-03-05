import graphene

from api.graphql.types.admin import AdminType
from api.graphql.util import WaverGraphQLResolveInfo


class AdminQ(graphene.ObjectType):
    admin = graphene.Field(AdminType)

    def resolve_admin(self, info: WaverGraphQLResolveInfo):
        return info.context.admin
