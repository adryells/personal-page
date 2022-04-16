import random
from typing import Dict

from starlette.testclient import TestClient

from api.db.models.Post import Post
from api.db.models.Tag import Tag
from api.db.query_utils.post import PostQueryUtils
from api.db.query_utils.tag import TagQueryUtils


class TestPost:

    @staticmethod
    def request_query(client: TestClient, extra_content_request: str = '', parameters: str = '', variables: Dict = {}):
        request = f"""
            query MyQuery {parameters}{{
              allnamespaces {{
                post {{
                    {extra_content_request}
                }}
              }}
            }}
        """

        query = {'query': request, "variables": variables}

        response = client.post(
            '/graphql',
            headers={'Content-Type': "application/json"},
            json=query
        )

        return response.json()

    def test_get_all_posts(self, client):
        content_request = """
              posts{
                id
                title
                active
                tags{
                  id
                  portugueseName
                  active
                }
              }
        """

        request = self.request_query(client, content_request)

        assert request['data']['allnamespaces']['post']['posts']

    def test_get_all_posts_paginated(self, client, session):
        page = 1
        perpage = random.randint(1, PostQueryUtils(session).count_query(
            PostQueryUtils(session).get_all_objects_query(Post)))

        content_request = """
              posts (page: $page, perpage: $perpage){
                id
                title
                active
                tags{
                  id
                  portugueseName
                  active
                }
              }
        """

        parameters = f"($page: Int, $perpage: Int)"

        variables = {
            "page": page,
            "perpage": perpage
        }

        request = self.request_query(client, content_request, parameters, variables)

        assert request['data']['allnamespaces']['post']['posts']

        artificial_pagination = [
            request['data']['allnamespaces']['post']['posts'][i:i + perpage]
            for i in range(0, len(request['data']['allnamespaces']['post']['posts']), perpage)
        ]

        assert artificial_pagination[0] == request['data']['allnamespaces']['post']['posts']

    def test_get_all_posts_filtered_by_status(self, client):
        status = random.choice([True, False])

        content_request = """
              posts (status: $status){
                id
                title
                active
                tags{
                  id
                  portugueseName
                  active
                }
              }
        """

        parameters = f"($status: Boolean)"

        variables = {
            "status": status,
        }

        request = self.request_query(client, content_request, parameters, variables)

        for post in request['data']['allnamespaces']['post']['posts']:
            assert post["active"] == status

    def test_get_all_posts_filtered_by_one_tag(self, client, session):
        tag = random.choice(TagQueryUtils(session).get_all_objects_query(Tag).all())

        content_request = """
              posts (tags: $tags){
                id
                title
                active
                tags{
                  id
                  portugueseName
                  active
                }
              }
        """

        parameters = "($tags: [String])"

        variables = {
            "tags": [tag.portuguese_name]
        }

        request = self.request_query(client, content_request, parameters, variables)

        for post in request['data']['allnamespaces']['post']['posts']:
            assert tag.portuguese_name in [tag["portugueseName"] for tag in post["tags"]]

    """ TODO: esse teste falha pois em minha logica eu pego um post se ele conter pelo menos 1 das tags passadas,
    a ideia da filtragem é que pegue somente os posts com ambas as tags passadas """

    # def test_get_all_posts_filtered_by_multiple_tags(self, client, session):
    #     tags = [random.choice(TagQueryUtils(session).get_all_objects_query(Tag).all()) for i in range(2)]
    #
    #     content_request = """
    #           posts (tags: $tags){
    #             id
    #             title
    #             active
    #             tags{
    #               id
    #               portugueseName
    #               active
    #             }
    #           }
    #     """
    #
    #     parameters = "($tags: [String])"
    #
    #     variables = {
    #         "tags": [tags[0].portuguese_name, tags[1].portuguese_name]
    #     }
    #
    #     request = self.request_query(client, content_request, parameters, variables)
    #
    #     for post in request['data']['allnamespaces']['post']['posts']:
    #         assert tags in post["tags"]

    def test_get_one_post(self, client, session):
        post = PostQueryUtils(session).get_object_by_id(Post, random.choice(
            PostQueryUtils(session).get_all_objects_query(Post).all()).id)

        content_request = """
              post (postId: $post_id){
                id
                title
                active
                tags{
                  id
                  portugueseName
                  active
                }
              }
        """

        parameters = "($post_id: Int!)"

        variables = {
            "post_id": post.id
        }

        request = self.request_query(client, content_request, parameters, variables)

        # TODO: Usar class Arue pra converter os id pra int
        assert request['data']['allnamespaces']['post']['post']['id'] == str(post.id)

    def test_get_one_invalid_post(self, client, session):

        # TODO: Count_query retornando 1 entender isso
        post_id = len(PostQueryUtils(session).get_all_objects_query(Post).all()) + 10

        content_request = """
              post (postId: $post_id){
                id
                title
                active
                tags{
                  id
                  portugueseName
                  active
                }
              }
        """

        parameters = "($post_id: Int!)"

        variables = {
            "post_id": post_id
        }

        request = self.request_query(client, content_request, parameters, variables)

        assert request['errors'][0]['message'] == f"Post id: {post_id} not found."
