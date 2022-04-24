import graphene

from api.controllers.projectcontroller import ProjectController
from api.graphql.types import ProjectType
from api.graphql.util import WaverGraphQLResolveInfo


class InputUpdateProject(graphene.InputObjectType):
    project_id = graphene.Int(required=True)
    title = graphene.String()
    english_title = graphene.String()
    description = graphene.String()
    english_description = graphene.String()
    bigdescription = graphene.String()
    english_bigdescription = graphene.String()
    link = graphene.String()
    media = graphene.String()
    active = graphene.Boolean()
    datecreated = graphene.DateTime()
    tags = graphene.List(graphene.String)


class InputAddProject(graphene.InputObjectType):
    title = graphene.String(required=True)
    english_title = graphene.String()
    description = graphene.String(required=True)
    english_description = graphene.String()
    bigdescription = graphene.String()
    english_bigdescription = graphene.String()
    link = graphene.String(required=True)
    media = graphene.String()
    active = graphene.Boolean()
    datecreated = graphene.DateTime()
    tags = graphene.List(graphene.String)


class UpdateProject(graphene.Mutation):
    class Arguments:
        data = InputUpdateProject()

    project = graphene.Field(ProjectType)

    def mutate(self, info: WaverGraphQLResolveInfo, data: InputUpdateProject):
        project = ProjectController(info.context.session).update_project(
            data.project_id,
            data.title,
            data.english_title,
            data.description,
            data.english_description,
            data.bigdescription,
            data.english_bigdescription,
            data.link,
            data.media,
            data.active,
            data.datecreated,
            data.tags,
        )

        return UpdateProject(project=project)


class AddProject(graphene.Mutation):
    class Arguments:
        data = InputAddProject()

    project = graphene.Field(ProjectType)

    def mutate(self, info: WaverGraphQLResolveInfo, data: InputAddProject):
        project = ProjectController(info.context.session).add_project(
            data.title,
            data.english_title,
            data.description,
            data.bigdescription,
            data.english_description,
            data.english_bigdescription,
            data.media,
            data.link,
            data.tags,
            data.datecreated,
            data.active
        )

        return AddProject(project=project)
