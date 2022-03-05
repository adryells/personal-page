import graphene

from api.db.models.Tag import Tag
from api.graphql.types import TagType
from api.graphql.util import WaverGraphQLResolveInfo


class TagQ(graphene.ObjectType):
    tags = graphene.List(TagType)
    tag = graphene.Field(TagType, tagid=graphene.Argument(graphene.Int))

    def resolve_tags(self, info: WaverGraphQLResolveInfo):
        return info.context.session.query(Tag).all()

    def resolve_tag(self, info: WaverGraphQLResolveInfo, tagid: int):
        return info.context.session.query(Tag).filter(Tag.tagid == tagid).one_or_none()