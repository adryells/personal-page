import graphene

from api.db.models.Tag import Tag
from api.graphql.types.tag import TagType
from api.graphql.util import WaverGraphQLResolveInfo


class Tag(graphene.ObjectType):
    tags = graphene.List(TagType)

    def resolve_tags(self, info: WaverGraphQLResolveInfo):
        return info.context.session.query(Tag).all()