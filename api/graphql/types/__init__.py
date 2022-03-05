from api.db.models.Admin import Admin
from api.db.models.HomeContent import HomeContent
from api.db.models.Post import Post
from api.db.models.Project import Project
from api.db.models.Social import Social
from api.db.models.Tag import Tag
from api.graphql.util import SQLAlchemyObjectArueType


class PostType(SQLAlchemyObjectArueType):
    class Meta:
        model = Post


class SocialType(SQLAlchemyObjectArueType):
    class Meta:
        model = Social


class ProjectType(SQLAlchemyObjectArueType):
    class Meta:
        model = Project


class TagType(SQLAlchemyObjectArueType):
    class Meta:
        model = Tag


class AdminType(SQLAlchemyObjectArueType):
    class Meta:
        model = Admin


class HomeContentType(SQLAlchemyObjectArueType):
    class Meta:
        model = HomeContent
