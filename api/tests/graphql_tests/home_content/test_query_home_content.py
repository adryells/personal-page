from starlette.testclient import TestClient


class TestHomeContent:

    @staticmethod
    def request_query(client: TestClient, extra_content_request: str = ''):
        request = \
            f"""
                query MyQuery {{
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

    def test_get_all_home_contents_paginated(self, client): ...

    def test_get_all_home_contents_filtered_by_status(self, client): ...
