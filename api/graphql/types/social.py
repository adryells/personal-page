from api.db.models.Social import Social
from api.graphql.util import SQLAlchemyObjectArueType


class SocialType(SQLAlchemyObjectArueType):
    class Meta:
        model = Social

