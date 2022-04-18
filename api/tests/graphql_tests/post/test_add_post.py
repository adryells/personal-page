from random import choice

from faker import Faker

from api.db.models.Tag import Tag
from api.db.query_utils.tag import TagQueryUtils


class TestAddHomeContent:

    def request_add_post(self, client, parameters: str = ''):
        query = f"""
            mutation MyMutation {{
              AddPost {parameters} {{
                post {{
                  active
                  content
                  datecreated
                  description
                  englishContent
                  englishDescription
                  id
                  englishTitle
                  media
                  title
                  tags {{
                    active
                    englishName
                    id
                    portugueseName
                  }}
                }}
              }}
            }}
        """

        request = {"query": query}

        response = client.post(
            '/graphql',
            headers={'Content-Type': "application/json"},
            json=request
        )

        return response.json()

    def test_add_post(self, client, session):
        chosen_tag = choice(
            TagQueryUtils(session).get_all_objects_query(Tag).all()
        )

        random_str = Faker().pystr()

        parameters = f"""
        (
            data: {{
                content: "{random_str}",
                description: "{random_str}",
                englishContent: "{random_str}",
                englishDescription: "{random_str}",
                englishTitle: "{random_str}",
                media: "{random_str}",
                tags: "[{chosen_tag.portuguese_name}]",
                title: "{random_str}"
            }}
        )
        """

        request = self.request_add_post(client, parameters)

        assert request['data']['AddPost']['post']