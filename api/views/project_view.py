import json

from fastapi import APIRouter
import requests

projects_router = APIRouter(
    prefix="/projects",
)


@projects_router.get('/')
def all_projects(page: int = None, perpage: int = None, status: bool = None, tags: str = None):
    variables = {
      "page": page,
      "perpage": perpage,
      "status": status,
      "tags": tags
    }

    data = {'query':
                """
                    query MyQuery ($page: Int, $perpage: Int, $status: Boolean, $tags: [String]){
                      allnamespaces {
                        project {
                          projects(page: $page, perpage: $perpage, status: $status, tags: $tags) {
                            active
                            bigdescription
                            description
                            datecreated
                            englishBigdescription
                            englishDescription
                            englishTitle
                            id
                            link
                            media
                            title
                            tags {
                              active
                              englishName
                              id
                              portugueseName
                            }
                          }
                        }
                      }
                    }
                """,
            'variables': variables}

    headers = {'Content-type': 'application/json'}

    response = requests.post("http://127.0.0.1:8081/graphql", data=json.dumps(data), headers=headers)

    return {'response': response.json()}


@projects_router.get('/<project_id>')
def get_post(project_id: str):

    variables = {"projectId": int(project_id)}

    data = {
        "query":"""
            query MyQuery($projectId: Int) {
              allnamespaces {
                project {
                  project(projectId: $projectId) {
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
                    tags {
                      active
                      englishName
                      portugueseName
                      id
                    }
                  }
                }
              }
            }

        """,
        'variables': variables
    }

    headers = {'Content-type': 'application/json'}

    response = requests.post("http://127.0.0.1:8081/graphql", data=json.dumps(data), headers=headers)

    return {'response': response.json()}
