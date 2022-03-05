from api.db.models.HomeContent import HomeContent
from api.graphql.util import SQLAlchemyObjectArueType


class HomeContentType(SQLAlchemyObjectArueType):
    class Meta:
        model = HomeContent
