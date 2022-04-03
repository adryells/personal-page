from typing import Dict

from starlette.testclient import TestClient


class TestProject:

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

    def test_get_all_projects(self, client): ...

    def test_get_all_projects_paginated(self, client): ...

    def test_get_all_projects_filtered_by_status(self, client): ...

    def test_get_all_projects_filtered_by_one_tag(self, client): ...

    def test_get_all_projects_filtered_by_multiple_tags(self, client): ...

    def test_get_one_project(self, client): ...

    def test_get_one_invalid_project(self, client): ...
