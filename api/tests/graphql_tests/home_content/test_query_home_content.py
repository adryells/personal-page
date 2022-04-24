import random

from starlette.testclient import TestClient

from api.db.models.HomeContent import HomeContent
from api.db.query_utils.homecontent import HomeContentQueryUtils


class TestHomeContent:

    @staticmethod
    def request_query(client: TestClient, extra_content_request: str = '', parameters: str = '', variables: dict = {}):
        request = \
            f"""
                query MyQuery {parameters}{{
                  allnamespaces {{
                    homeContent {{
                        {extra_content_request}
                    }}
                  }}
                }}
            """

        query = {'query': request, 'variables': variables}

        response = client.post(
            '/graphql',
            headers={'Content-Type': "application/json"},
            json=query
        )

        return response.json()

    def test_get_all_home_contents(self, client):
        content_request = """
            homeContents {
                id
                content
                homecontenttype
                active
                datecreated
              }
        """
        request = self.request_query(client, content_request)

        assert request['data']['allnamespaces']['homeContent']['homeContents']

    def test_get_all_home_contents_paginated_with_page_1(self, client, session):

        page = 1
        perpage = random.randint(1, HomeContentQueryUtils(session).count_query(
            HomeContentQueryUtils(session).get_all_objects_query(HomeContent)))

        content_request = """
                    homeContents (page: $page, perpage: $perpage){
                        id
                        content
                        homecontenttype
                        active
                        datecreated
                      }
                """

        parameters = f"($page: Int, $perpage: Int)"

        variables = {
            "page": page,
            "perpage": perpage
        }

        request = self.request_query(client, content_request, parameters, variables)

        assert request['data']['allnamespaces']['homeContent']['homeContents']

        artificial_pagination = [
            request['data']['allnamespaces']['homeContent']['homeContents'][i:i + perpage]
            for i in range(0, len(request['data']['allnamespaces']['homeContent']['homeContents']), perpage)
        ]

        assert artificial_pagination[0] == request['data']['allnamespaces']['homeContent']['homeContents']

    # TODO: Develop a test for page bigger than 1 or improve the existent

    # TODO: This is currently failing
    def test_get_all_home_contents_filtered_by_status(self, client):
        status = random.choice([True, False])

        content_request = """
                            homeContents (status: $status){
                                id
                                content
                                homecontenttype
                                active
                                datecreated
                              }
                        """

        parameters = f"($status: Boolean)"

        variables = {
            "status": status,
        }

        request = self.request_query(client, content_request, parameters, variables)

        for homecontent in request['data']['allnamespaces']['homeContent']['homeContents']:
            assert homecontent["active"] == status
