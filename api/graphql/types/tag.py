from api.db.models.Tag import Tag
from api.graphql.util import SQLAlchemyObjectArueType


class TagType(SQLAlchemyObjectArueType):
    class Meta:
        model = Tag

