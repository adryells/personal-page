from random import choice


from api.db.models.Post import Post
from api.db.models.Project import Project
from api.db.query_utils.post import PostQueryUtils
from api.db.query_utils.project import ProjectQueryUtils


class TestAddHomeContent:

    def request_remove_tag_from(self, client, parameters: str = '', extra_params: str = '', variables: dict = {}):
        query = f"""
            mutation MyMutation {parameters}{{
              RemoveTag {extra_params} {{
                success
              }}
            }}
        """

        request = {"query": query, "variables": variables}

        response = client.post(
            '/graphql',
            headers={'Content-Type': "application/json"},
            json=request
        )

        return response.json()

    def test_remove_tag_from_post_success(self, client, session):
        post = choice(
            PostQueryUtils(session).get_all_objects_query(Post).all()
        )

        variables = {
            "tagid": choice(post.tags).id,
            "postid": post.id
        }

        parameters = "($tagid: Int!, $postid: Int)"

        extra_params = "(tagId: $tagid, postId: $postid)"

        request = self.request_remove_tag_from(client, parameters, extra_params, variables)

        assert request['data']['RemoveTag']['success']

    def test_remove_tag_from_project_success(self, client, session):
        project = choice(
            ProjectQueryUtils(session).get_all_objects_query(Project).all()
        )

        variables = {
            "tagid": choice(project.tags).id,
            "projectid": project.id
        }

        parameters = "($tagid: Int!, $projectid: Int)"

        extra_params = "(tagId: $tagid, projectId: $projectid)"

        request = self.request_remove_tag_from(client, parameters, extra_params, variables)

        assert request['data']['RemoveTag']['success']

    def test_update_tag_with_invalid_post_id(self, client, session):
        invalid_post_id = len(
            PostQueryUtils(session).get_all_objects_query(Post).all()
        ) + 10

        variables = {
            "tagid": 1,
            "postid": invalid_post_id
        }

        parameters = "($tagid: Int!, $postid: Int)"

        extra_params = "(tagId: $tagid, postId: $postid)"

        request = self.request_remove_tag_from(client, parameters, extra_params, variables)

        assert request['errors'][0]['message'] == f"Post id: {invalid_post_id} not found."

    def test_update_tag_with_invalid_project_id(self, client, session):
        invalid_project_id = len(
            ProjectQueryUtils(session).get_all_objects_query(Project).all()
        ) + 10

        variables = {
            "tagid": 1,
            "projectid": invalid_project_id
        }

        parameters = "($tagid: Int!, $projectid: Int)"

        extra_params = "(tagId: $tagid, projectId: $projectid)"

        request = self.request_remove_tag_from(client, parameters, extra_params, variables)

        assert request['errors'][0]['message'] == f"Project id: {invalid_project_id} not found."

