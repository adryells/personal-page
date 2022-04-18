from random import choice, randint
from typing import Dict

from starlette.testclient import TestClient

from api.db.models.Tag import Tag
from api.db.query_utils.tag import TagQueryUtils


class TestTag:

    @staticmethod
    def request_query_all_tags(client: TestClient, parameters: str = ''):
        request = f"""
            query MyQuery {{
              allnamespaces {{
                tag {{
                  tags  {parameters} {{
                    id
                    active
                    portugueseName
                    englishName
                  }}
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

    @staticmethod
    def request_query_one_tag(client: TestClient, parameters: str = ''):
        request = f"""
                query MyQuery {{
                  allnamespaces {{
                    tag {{
                      tag  {parameters} {{
                        id
                        active
                        portugueseName
                        englishName
                      }}
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

    def test_get_all_tags(self, client):
        request = self.request_query_all_tags(client)

        assert request['data']['allnamespaces']['tag']['tags']

    def test_get_all_tags_paginated(self, client, session):
        perpage = randint(1, TagQueryUtils(session).count_query(TagQueryUtils(session).get_all_objects_query(Tag)))
        parameters = f"(page: 1, perpage: {perpage})"

        request = self.request_query_all_tags(client, parameters)

        assert request['data']['allnamespaces']['tag']['tags']

        artificial_pagination = [
            request['data']['allnamespaces']['tag']['tags'][i:i + perpage]
            for i in range(0, len(request['data']['allnamespaces']['tag']['tags']), perpage)
        ]

        assert artificial_pagination[0] == request['data']['allnamespaces']['tag']['tags']

    # TO DO THIS LOGIC CHANGE TO ENUM OR STRING IM CONTROLLER
    # def test_get_all_tags_filtered_by_status(self, client):
    #     status = choice([True, False])
    #
    #     parameters = f"(active: true)"
    #
    #     request = self.request_query(client, parameters)
    #
    #     for tag in request['data']['allnamespaces']['tag']['tags']:
    #         assert tag["active"] == status

    def test_get_one_tag(self, client, session):
        tagid = choice(TagQueryUtils(session).get_all_objects_query(Tag).all()).id

        request = self.request_query_one_tag(client, f'(tagid:{tagid})')

        assert request['data']['allnamespaces']['tag']['tag']['id'] == str(tagid)

    def test_get_one_invalid_tag(self, client, session):
        tagid = len(TagQueryUtils(session).get_all_objects_query(Tag).all()) + 10

        request = self.request_query_one_tag(client, f'(tagid:{tagid})')

        assert request['errors'][0]['message'] == f'Tag id: {tagid} not found.'
