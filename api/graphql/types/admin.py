from api.db.models.Admin import Admin
from api.graphql.util import SQLAlchemyObjectArueType


class AdminType(SQLAlchemyObjectArueType):
    class Meta:
        model = Admin