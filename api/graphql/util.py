from dataclasses import dataclass
from typing import Any, Union, Type

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import ResolveInfo
from sqlalchemy.orm import Session
from starlette.requests import HTTPConnection

from api.db.models.Admin import Admin


def MountGraphQLObject(object_type: Union[Type[graphene.Mutation], Type[graphene.ObjectType]]):
    is_mutation = issubclass(object_type, graphene.Mutation)

    relation_name = object_type.__name__.lower() if not is_mutation else object_type.__name__

    object_properties = {
        f'{relation_name}': graphene.Field(object_type) if not is_mutation else object_type.Field(),
        f'resolve_{relation_name}': lambda _, __: object_type
    }

    return type(
        f'{relation_name}Mount', tuple(), object_properties
    )


@dataclass
class GraphQLAppContext:
    session: Session
    background: Any
    request: HTTPConnection
    admin: Admin = None
    authorization: str = None

    # necessary because graphene needs context to have this method
    def get(self, o: str):
        return getattr(self, o, None)

    def __getitem__(self, key: str):
        return self.get(key)


class WaverGraphQLResolveInfo(ResolveInfo):
    context: GraphQLAppContext


class SQLAlchemyObjectArueType(SQLAlchemyObjectType):
    class Meta:
        abstract = True

    id = graphene.Field(graphene.Int, required=True)