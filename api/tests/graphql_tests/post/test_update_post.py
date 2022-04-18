from random import choice

from faker import Faker

from api.db.models.Post import Post
from api.db.models.Tag import Tag
from api.db.query_utils.post import PostQueryUtils
from api.db.query_utils.tag import TagQueryUtils


class TestAddHomeContent:

    def request_update_post(self, client, parameters: str = ''):
        query = f"""
            mutation MyMutation {{
              UpdatePost {parameters} {{
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

    def test_update_post(self, client, session):
        chosen_tag = choice(
            TagQueryUtils(session).get_all_objects_query(Tag).all()
        )

        chosen_post = choice(
            PostQueryUtils(session).get_all_objects_query(Post).all()
        )

        random_str = Faker().pystr()

        parameters = f"""
        (
            data: {{
                postId: {chosen_post.id}
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

        request = self.request_update_post(client, parameters)

        session.refresh(chosen_post)

        assert request['data']['UpdatePost']['post']['content']
        assert chosen_post.content == random_str

        assert request['data']['UpdatePost']['post']['description']
        assert chosen_post.description == random_str

        assert request['data']['UpdatePost']['post']['media']
        assert chosen_post.media == random_str

        assert request['data']['UpdatePost']['post']['title']
        assert chosen_post.title == random_str

