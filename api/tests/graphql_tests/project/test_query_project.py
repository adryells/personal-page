import random
from typing import Dict

from starlette.testclient import TestClient

from api.db.models.Project import Project
from api.db.models.Tag import Tag
from api.db.query_utils.project import ProjectQueryUtils
from api.db.query_utils.tag import TagQueryUtils


class TestProject:

    @staticmethod
    def request_query(client: TestClient, extra_content_request: str = '', parameters: str = '', variables: Dict = {}):
        request = f"""
            query MyQuery {parameters}{{
              allnamespaces {{
                project {{
                  {extra_content_request}
                }}
              }}
            }}
        """

        query = {'query': request, "variables": variables}

        response = client.post(
            '/graphql',
            headers={'Content-Type': "application/json"},
            json=query
        )

        return response.json()

    def test_get_all_projects(self, client):
        content_request = """
            projects {
                id
                title
                link
                media
                description
                datecreated
                active
          }
        """
        request = self.request_query(client, content_request)

        assert request['data']['allnamespaces']['project']['projects']

    def test_get_all_projects_paginated(self, client,session):
        page = 1
        perpage = random.randint(1, ProjectQueryUtils(session).count_query(
            ProjectQueryUtils(session).get_all_objects_query(Project)))

        content_request = """
            projects (page: $page, perpage: $perpage){
                id
                title
                link
                media
                description
                datecreated
                active
          }
        """

        parameters = f"($page: Int, $perpage: Int)"

        variables = {
            "page": page,
            "perpage": perpage
        }

        request = self.request_query(client, content_request, parameters, variables)

        assert request['data']['allnamespaces']['project']['projects']

        artificial_pagination = [
            request['data']['allnamespaces']['project']['projects'][i:i + perpage]
            for i in range(0, len(request['data']['allnamespaces']['project']['projects']), perpage)
        ]

        assert artificial_pagination[0] == request['data']['allnamespaces']['project']['projects']

    def test_get_all_projects_filtered_by_status(self, client):
        status = random.choice([True, False])

        content_request = """
          projects (status: $status){
            id
            title
            link
            media
            description
            datecreated
            active
          }
        """

        parameters = f"($status: Boolean)"

        variables = {
            "status": status,
        }

        request = self.request_query(client, content_request, parameters, variables)

        for project in request['data']['allnamespaces']['project']['projects']:
            assert project["active"] == status

    def test_get_all_projects_filtered_by_one_tag(self, client,session):
        tag = random.choice(TagQueryUtils(session).get_all_objects_query(Tag).all())

        content_request = """
              projects (tags: $tags){
                id
                title
                link
                media
                description
                datecreated
                active
                tags{
                    id
                    portugueseName
                }
              }
        """

        parameters = "($tags: [String])"

        variables = {
            "tags": [tag.portuguese_name]
        }

        request = self.request_query(client, content_request, parameters, variables)

        for project in request['data']['allnamespaces']['project']['projects']:
            assert tag.portuguese_name in [tag["portugueseName"] for tag in project["tags"]]

    # TODO: Same situaation in this test of post
    # def test_get_all_projects_filtered_by_multiple_tags(self, client): ...

    def test_get_one_project(self, client,session):
        project = ProjectQueryUtils(session).get_object_by_id(Project, random.choice(
            ProjectQueryUtils(session).get_all_objects_query(Project).all()).id)

        content_request = """
                      project (projectId: $project_id){
                        id
                        title
                        active
                        tags{
                          id
                          portugueseName
                          active
                        }
                      }
                """

        parameters = "($project_id: Int!)"

        variables = {
            "project_id": project.id
        }

        request = self.request_query(client, content_request, parameters, variables)

        assert request['data']['allnamespaces']['project']['project']['id'] == str(project.id)

    def test_get_one_invalid_project(self, client, session):
        project_id = len(ProjectQueryUtils(session).get_all_objects_query(Project).all()) + 10

        content_request = """
              project (projectId: $project_id){
                id
                title
                active
                tags{
                  id
                  portugueseName
                  active
                }
              }
        """

        parameters = "($project_id: Int!)"

        variables = {
            "project_id": project_id
        }

        request = self.request_query(client, content_request, parameters, variables)

        assert request['errors'][0]['message'] == f"Project id: {project_id} not found."

