from random import choice

from faker import Faker

from api.db.models.HomeContent import HomeContent, HomeContentType
from api.db.query_utils.homecontent import HomeContentQueryUtils


class TestUpdateHomeContent:
    def request_update_home_content(self, client, variables: dict = {}):
        query = """
            mutation MyMutation ($active: Boolean, $content: String, $datecreated: DateTime, $homecontenttype: String, $hcid: Int!){
              UpdateHomeContent(data: {active: $active, content: $content, datecreated: $datecreated, homecontenttype: $homecontenttype, homecontentId: $hcid}) {
                homecontent {
                  active
                  content
                  datecreated
                  homecontenttypeId
                  id
                }
              }
            }
        """

        request = {"query": query, "variables": variables}

        response = client.post(
            '/graphql',
            headers={'Content-Type': "application/json"},
            json=request
        )

        return response.json()

    def test_update_home_content_success(self, client, session):
        actual_home_content = choice(HomeContentQueryUtils(session).get_all_objects_query(HomeContent).all())
        home_content_type = HomeContentQueryUtils(session).get_random_register_from_table(HomeContentType)

        variables = {
            "content": Faker().pystr(),
            "homecontenttype": home_content_type.slug,
            "active": choice([True, False]),
            "hcid": actual_home_content.id
        }

        request = self.request_update_home_content(client, variables)

        assert request['data']['UpdateHomeContent']['homecontent']['active'] == variables["active"]
        assert request['data']['UpdateHomeContent']['homecontent']['homecontenttypeId'] == home_content_type.id
        assert request['data']['UpdateHomeContent']['homecontent']['content'] == variables["content"]

    def test_update_home_content_with_invalid_home_content(self, client, session):
        invalid_home_content_id = len(HomeContentQueryUtils(session).get_all_objects_query(HomeContent).all()) + 10

        variables = {
            "content": Faker().pystr(),
            "homecontenttype": choice(["whoido", "whoiam"]),
            "active": choice([True, False]),
            "hcid": invalid_home_content_id
        }

        request = self.request_update_home_content(client, variables)

        assert request['errors'][0]['message'] == "Home Content not found."
