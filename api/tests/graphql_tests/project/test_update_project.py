from random import choice

from faker import Faker

from api.db.models.Project import Project
from api.db.models.Tag import Tag
from api.db.query_utils.project import ProjectQueryUtils
from api.db.query_utils.tag import TagQueryUtils


class TestAddHomeContent:

    def request_add_project(self, client, parameters: str = ''):
        query = f"""
            mutation MyMutation {{
              UpdateProject {parameters}{{
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

    def test_update_project_success(self, client, session):
        chosen_tag = choice(
            TagQueryUtils(session).get_all_objects_query(Tag).all()
        )

        chosen_project = choice(
            ProjectQueryUtils(session).get_all_objects_query(Project).all()
        )

        random_str = Faker().pystr()

        parameters = f"""(
            data: {{
                projectId: {chosen_project.id}
                title: "{random_str}",
                description: "{random_str}",
                link: "{Faker().url()}",
                active: true,
                bigdescription: "{random_str}",
                englishBigdescription: "{random_str}",
                englishDescription: "{random_str}", 
                englishTitle: "{random_str}",
                media: "{random_str}",
                tags: "{chosen_tag.portuguese_name}"
                }}
            )
        """

        request = self.request_add_project(client, parameters)

        session.refresh(chosen_project)

        assert request['data']['UpdateProject']['project']["title"] == random_str
        assert chosen_project.title == random_str

        assert request['data']['UpdateProject']['project']["description"] == random_str
        assert chosen_project.description == random_str

        assert request['data']['UpdateProject']['project']["bigdescription"] == random_str
        assert chosen_project.bigdescription == random_str

        assert request['data']['UpdateProject']['project']["media"] == random_str
        assert chosen_project.media == random_str
