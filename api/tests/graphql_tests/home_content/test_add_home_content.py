from random import choice

from faker import Faker

from api.db.models.HomeContent import HomeContentType
from api.db.query_utils.homecontent import HomeContentQueryUtils


class TestAddHomeContent:
    def request_add_home_content(self, client, variables: dict = {}):
        query = """
            mutation MyMutation ($content: String!, $homecontenttype: String!, $active: Boolean, $datecreated: DateTime){
              AddHomeContent(data: {content: $content, homecontenttype: $homecontenttype, active: $active, datecreated: $datecreated}) {
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

    def test_add_home_content_success(self, client, session):
        home_content_type = HomeContentQueryUtils(session).get_random_register_from_table(HomeContentType)
        variables = {
            "content": Faker().pystr(),
            "homecontenttype": home_content_type.slug,
            "active": choice([True, False])
        }

        request = self.request_add_home_content(client, variables)

        # TODO: This failling
        assert request['data']['AddHomeContent']['homecontent']['active'] == variables["active"]
        assert request['data']['AddHomeContent']['homecontent']['homecontenttypeId'] == home_content_type.id
        assert request['data']['AddHomeContent']['homecontent']['content'] == variables["content"]
