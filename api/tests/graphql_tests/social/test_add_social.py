from random import choice

from faker import Faker


class TestAddHomeContent:
    def request_add_home_content(self, client, variables: dict = {}):
        query = """
            mutation MyMutation ($name: String!, $link: String!, $media: String!, $active: Boolean){
              AddSocial(data: {name: $name, link: $link, media: $media, active: $active}) {
                social {
                  active
                  id
                  link
                  media
                  name
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

    def test_add_social_success(self, client):
        variables = {
            "name": Faker("pt-br").name(),
            "media": Faker().pystr(),
            "link": Faker().file_path(),
            "active": choice([True, False])
        }

        request = self.request_add_home_content(client, variables)

        assert request['data']['AddSocial']['social']['active'] == variables["active"]
        assert request['data']['AddSocial']['social']['media'] == variables["media"]
        assert request['data']['AddSocial']['social']['link'] == variables["link"]
        assert request['data']['AddSocial']['social']['name'] == variables["name"]
