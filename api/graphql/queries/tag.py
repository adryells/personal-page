import graphene

from api.db.models.Tag import Tag
from api.graphql.types import TagType
from api.graphql.util import WaverGraphQLResolveInfo


class TagQ(graphene.ObjectType):
    tags = graphene.List(TagType,
                         page=graphene.Argument(graphene.Int, default_value=1),
                         perpage=graphene.Argument(graphene.Int, default_value=50)
                         )
    tag = graphene.Field(TagType, tagid=graphene.Argument(graphene.Int))

    def resolve_tags(self, info: WaverGraphQLResolveInfo, page: int, perpage: int):
        return info.context.session.query(Tag).limit(perpage).offset((page-1) * perpage).all()

    def resolve_tag(self, info: WaverGraphQLResolveInfo, tagid: int):
        return info.context.session.query(Tag).filter(Tag.tagid == tagid).one_or_none()