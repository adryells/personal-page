import graphene

from api.controllers.homecontentcontroller import HomeContentController
from api.graphql.types import HomeContentType
from api.graphql.util import WaverGraphQLResolveInfo


class InputAddHomeContent(graphene.InputObjectType):
    content = graphene.String(required=True)
    homecontenttype = graphene.String(required=True)
    active = graphene.Boolean(default_value=True)
    datecreated = graphene.String()


class InputUpdateHomeContent(graphene.InputObjectType):
    homecontent_id = graphene.Int()
    content = graphene.String()
    homecontenttype = graphene.String()
    active = graphene.Boolean()
    datecreated = graphene.String()


class AddHomeContent(graphene.Mutation):
    class Arguments:
        data = InputAddHomeContent()

    homecontent = graphene.Field(HomeContentType)

    def mutate(self, info: WaverGraphQLResolveInfo, data: InputAddHomeContent):
        homecontent = HomeContentController(info.context.session).add_home_content(
            content=data.content,
            homecontenttype=data.homecontenttype,
            active=data.active,
            datecreated=data.datecreated
        )

        return AddHomeContent(homecontent=homecontent)


class UpdateHomeContent(graphene.Mutation):
    class Arguments:
        data = InputUpdateHomeContent()

    homecontent = graphene.Field(HomeContentType)

    def mutate(self, info: WaverGraphQLResolveInfo, data: InputUpdateHomeContent):
        homecontent = HomeContentController(info.context.session).update_home_content(
            home_content_id=data.homecontent_id,
            content=data.content,
            homecontenttype=data.homecontenttype,
            active=data.active,
            datecreated=data.datecreated
        )

        return UpdateHomeContent(homecontent=homecontent)
