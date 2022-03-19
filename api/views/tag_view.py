import json

from fastapi import APIRouter
import requests

tag_router = APIRouter(
    prefix="/tags",
)


@tag_router.get('/')
def all_tags():
    data = {'query':
                """
                    query MyQuery {
                      allnamespaces {
                        tag {
                          tags {
                            id
                            portugueseName
                            englishName
                            active
                          }
                        }
                      }
                    }
        
                """}

    headers = {'Content-type': 'application/json'}

    response = requests.post("http://127.0.0.1:8081/graphql", data=json.dumps(data), headers=headers)

    return {'response': response.json()}


