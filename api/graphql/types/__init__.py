from graphene_sqlalchemy import SQLAlchemyObjectType

from api.db.models.Admin import Admin
from api.db.models.HomeContent import HomeContent
from api.db.models.Post import Post
from api.db.models.Project import Project
from api.db.models.Social import Social
from api.db.models.Tag import Tag


class PostType(SQLAlchemyObjectType):
    class Meta:
        model = Post


class SocialType(SQLAlchemyObjectType):
    class Meta:
        model = Social


class ProjectType(SQLAlchemyObjectType):
    class Meta:
        model = Project


class TagType(SQLAlchemyObjectType):
    class Meta:
        model = Tag


class AdminType(SQLAlchemyObjectType):
    class Meta:
        model = Admin


class HomeContentType(SQLAlchemyObjectType):
    class Meta:
        model = HomeContent
