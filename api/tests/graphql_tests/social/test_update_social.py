from random import choice

from faker import Faker

from api.db.models.Social import Social
from api.db.query_utils.social import SocialQueryUtils


class TestAddSocial:
    def request_update_social(self, client, variables: dict = {}):
        query = """
            mutation MyMutation ($name: String, $link: String, $media: String, $active: Boolean, $socialid: Int!){
              UpdateSocial(data: {name: $name, link: $link, media: $media, active: $active, socialId: $socialid}) {
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

    def test_update_social_success(self, client, session):
        actual_social_id = choice(
            SocialQueryUtils(session).get_all_objects_query(Social).all()
        ).id

        variables = {
            "name": Faker("pt-br").name(),
            "media": Faker().pystr(),
            "link": Faker().file_path(),
            "active": choice([True, False]),
            "socialid": actual_social_id
        }

        request = self.request_update_social(client, variables)

        assert request['data']['UpdateSocial']['social']['active'] == variables["active"]
        assert request['data']['UpdateSocial']['social']['media'] == variables["media"]
        assert request['data']['UpdateSocial']['social']['link'] == variables["link"]
        assert request['data']['UpdateSocial']['social']['name'] == variables["name"]

    def test_update_social_with_invalid_id(self, client, session):
        invalid_social_id = len(
            SocialQueryUtils(session).get_all_objects_query(Social).all()
        ) + 10

        variables = {
            "name": Faker("pt-br").name(),
            "media": Faker().pystr(),
            "link": Faker().file_path(),
            "active": choice([True, False]),
            "socialid": invalid_social_id
        }

        request = self.request_update_social(client, variables)

        assert request['errors'][0]['message'] == f"Social id: {invalid_social_id} not found."
