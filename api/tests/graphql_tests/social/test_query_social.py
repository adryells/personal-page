import random
from typing import Dict

from starlette.testclient import TestClient

from api.db.models.Social import Social
from api.db.query_utils.social import SocialQueryUtils


class TestSocial:

    @staticmethod
    def request_query(client: TestClient, extra_content_request: str = '', parameters: str = '', variables: Dict = {}):
        request = f"""
            query MyQuery {parameters}{{
              allnamespaces {{
                social {{
                  {extra_content_request}
                }}
              }}
            }}
        """

        query = {"query": request, "variables": variables}

        response = client.post(
            '/graphql',
            headers={'Content-Type': "application/json"},
            json=query
        )

        return response.json()

    def test_get_all_socials(self, client, session):
        content_request = """
            socials{
                id
                link
                media
                name
            }
        """

        request = self.request_query(client, content_request)

        assert request['data']['allnamespaces']['social']['socials']

    # TODO: resolve "query is not defined"
    # def test_get_all_socials_paginated(self, client, session):
    #     page = 1
    #     perpage = random.randint(
    #         1, len(SocialQueryUtils(session).get_all_objects_query(Social).all())
    #     )
    #
    #     content_request = """
    #         socials (page: $page, perpage: $perpage){
    #             id
    #             link
    #             media
    #             name
    #         }
    #     """
    #
    #     parameters = "($page: Int, $perpage: Int)"
    #
    #     variables = {
    #         "page": page,
    #         "perpage": perpage
    #     }
    #
    #     request = self.request_query(client, content_request, parameters, variables)
    #
    #     assert request['data']['allnamespaces']['social']['socials']
    #
    #     artificial_pagination = [
    #         request['data']['allnamespaces']['social']['socials'][i:i + perpage]
    #         for i in range(0, len(request['data']['allnamespaces']['social']['socials']), perpage)
    #     ]
    #
    #     assert artificial_pagination[0] == request['data']['allnamespaces']['social']['socials']

    def test_get_one_social(self, client, session):
        socialid = random.choice(
            SocialQueryUtils(session).get_all_objects_query(Social).all()
        ).id
        content_request = f"""
            social (socialId:{socialid}){{
                id
                name
                link
                media
                active
              }}
        """

        request = self.request_query(client, content_request)

        assert request['data']['allnamespaces']['social']['social']['id'] == str(socialid)


    def test_get_one_invalid_social(self, client): ...
