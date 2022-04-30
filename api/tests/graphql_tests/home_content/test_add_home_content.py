from random import choice

from faker import Faker


class TestAddHomeContent:
    def request_add_home_content(self, client, variables: dict = {}):
        query = """
            mutation MyMutation ($content: String!, $homecontenttype: String!, $active: Boolean, $datecreated: DateTime){
              AddHomeContent(data: {content: $content, homecontenttype: $homecontenttype, active: $active, datecreated: $datecreated}) {
                homecontent {
                  active
                  content
                  datecreated
                  homecontenttype
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

    def test_add_home_content_success(self, client):
        variables = {
            "content": Faker().pystr(),
            "homecontenttype": choice(["whoiam", "whatido"]),
            "active": choice([True, False])
        }

        request = self.request_add_home_content(client, variables)

        # TODO: This failling
        assert request['data']['AddHomeContent']['homecontent']['active'] == variables["active"]
        assert request['data']['AddHomeContent']['homecontent']['homecontenttype'] == variables["homecontenttype"]
        assert request['data']['AddHomeContent']['homecontent']['content'] == variables["content"]
