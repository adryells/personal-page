from api.db.models.Post import Post
from api.graphql.util import SQLAlchemyObjectArueType


class PostType(SQLAlchemyObjectArueType):
    class Meta:
        model = Post