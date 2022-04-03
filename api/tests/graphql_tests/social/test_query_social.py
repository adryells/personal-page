from typing import Dict

from starlette.testclient import TestClient


class TestSocial:

    @staticmethod
    def request_query(client: TestClient, extra_content_request: str = '', variables: Dict = {}):
        request = ""

        query = {'query': request, "variables": variables}

        response = client.post(
            '/graphql',
            headers={'Content-Type': "application/json"},
            json=query
        )

        return response.json()

    def test_get_all_socials(self, client): ...

    def test_get_all_socials_paginated(self, client): ...

    def test_get_one_social(self, client): ...

    def test_get_one_invalid_social(self, client): ...
