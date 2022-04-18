from random import choice

from faker import Faker

from api.db.models.Tag import Tag
from api.db.query_utils.tag import TagQueryUtils


class TestAddHomeContent:

    def request_add_project(self, client, parameters: str = ''):
        query = f"""
            mutation MyMutation {{
              AddProject {parameters}{{
                project {{
                  active
                  bigdescription
                  datecreated
                  description
                  englishBigdescription
                  englishDescription
                  englishTitle
                  id
                  link
                  media
                  title
                  tags {{
                    active
                    englishName
                    portugueseName
                    id
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

    def test_add_project(self, client, session):
        chosen_tag = choice(
            TagQueryUtils(session).get_all_objects_query(Tag).all()
        )

        parameters = f"""(
            data: {{
                title: "{Faker().pystr()}",
                description: "{Faker().pystr()}",
                link: "{Faker().url()}",
                active: true,
                bigdescription: "{Faker().pystr()}",
                englishBigdescription: "{Faker().pystr()}",
                englishDescription: "{Faker().pystr()}", 
                englishTitle: "{Faker().pystr()}",
                media: "{Faker().pystr()}",
                tags: "{[chosen_tag.portuguese_name]}"
                }}
            )
        """

        request = self.request_add_project(client, parameters)

        assert request['data']['AddProject']['project']