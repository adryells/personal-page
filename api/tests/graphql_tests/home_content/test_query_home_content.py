import random

from starlette.testclient import TestClient

from api.db.models.HomeContent import HomeContent
from api.db.query_utils.homecontent import HomeContentQueryUtils


class TestHomeContent:

    @staticmethod
    def request_query(client: TestClient, extra_content_request: str = '', parameters: str = ''):
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

        query = {'query': request}

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

        # TODO: Test actually, improve an implement this test

        page = 1
        perpage = random.randint(1, HomeContentQueryUtils(session).count_query(
            HomeContentQueryUtils.get_all_objects_query(HomeContent)))

        content_request = """
                    homeContents {
                        id
                        content
                        homecontenttype
                        active
                        datecreated
                      }
                """

        parameters = f"(page: {page}, perpage: {perpage})"

        request = self.request_query(client, content_request, parameters)

        assert request['data']['allnamespaces']['homeContent']['homeContents']

        artificial_pagination = [['data']['allnamespaces']['homeContent']['homeContents'][i:i + perpage] for i in
                                 range(0, len(['data']['allnamespaces']['homeContent']['homeContents']), perpage)]

        assert artificial_pagination[0] == request['data']['allnamespaces']['homeContent']['homeContents']

    def test_get_all_home_contents_filtered_by_status(self, client): ...
