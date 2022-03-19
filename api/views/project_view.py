import json

from fastapi import APIRouter
import requests

projects_router = APIRouter(
    prefix="/projects",
)


@projects_router.get('/')
def all_projects():
    data = {'query':
                """
                    query MyQuery {
                      allnamespaces {
                        project {
                          projects {
                            id
                            title
                            active
                            media
                            link
                            description
                            bigdescription
                            datecreated
                            englishBigdescription
                            englishDescription
                            englishTitle
                          }
                        }
                      }
                    }
        
                """}

    headers = {'Content-type': 'application/json'}

    response = requests.post("http://127.0.0.1:8081/graphql", data=json.dumps(data), headers=headers)

    return {'response': response.json()}


