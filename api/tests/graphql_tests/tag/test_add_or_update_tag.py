from random import choice

from faker import Faker

from api.db.models.Tag import Tag
from api.db.query_utils.tag import TagQueryUtils


class TestAddOrUpdateTag:

    def request_add_or_update_tag(self, client, variables: dict = {}):
        query = """
            mutation MyMutation ($pt_name: String!, $en_name: String, $active: Boolean){
              AddOrUpdateTag(data: {portugueseName: $pt_name, active: $active, englishName: $en_name}) {
                tag {
                  active
                  englishName
                  id
                  portugueseName
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

    def test_add_tag_success(self, client):
        variables = {
            "pt_name": Faker("pt-br").name(),
            "en_name": Faker().name(),
            "active": choice([True, False])
        }

        request = self.request_add_or_update_tag(client, variables)

        assert request['data']['AddOrUpdateTag']['tag']['active'] == variables["active"]
        assert request['data']['AddOrUpdateTag']['tag']['englishName'] == variables["en_name"]
        assert request['data']['AddOrUpdateTag']['tag']['portugueseName'] == variables["pt_name"]

    def test_update_tag_success(self, client, session):
        existent_tag: Tag = choice(
            TagQueryUtils(session).get_all_objects_query(Tag).all()
        )

        variables = {
            "pt_name": existent_tag.portuguese_name,
            "en_name": Faker().name(),
            "active": False if existent_tag.active else True
        }

        request = self.request_add_or_update_tag(client, variables)

        session.refresh(existent_tag)

        assert request['data']['AddOrUpdateTag']['tag']['active'] == variables["active"]
        assert request['data']['AddOrUpdateTag']['tag']['active'] == existent_tag.active

        assert request['data']['AddOrUpdateTag']['tag']['englishName'] == variables["en_name"]
        assert request['data']['AddOrUpdateTag']['tag']['englishName'] == existent_tag.english_name

        assert request['data']['AddOrUpdateTag']['tag']['portugueseName'] == variables["pt_name"]
        assert request['data']['AddOrUpdateTag']['tag']['portugueseName'] == existent_tag.portuguese_name

