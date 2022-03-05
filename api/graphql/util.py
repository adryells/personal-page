from dataclasses import dataclass
from typing import Any, Union, Type

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLResolveInfo
from sqlalchemy.orm import Session
from starlette.requests import HTTPConnection, Request
from starlette.websockets import WebSocket

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
    ws: WebSocket = None
    session: Session = None
    background: Any = None
    request: Request = None
    admin: Admin = None
    authorization: str = None

    def get(self, o: str):
        return getattr(self, o, None)

    def __getitem__(self, key: str):
        return self.get(key)


class WaverGraphQLResolveInfo(GraphQLResolveInfo):
    context: GraphQLAppContext


class SQLAlchemyObjectArueType(SQLAlchemyObjectType):
    class Meta:
        abstract = True

    id = graphene.Field(graphene.Int, required=True)