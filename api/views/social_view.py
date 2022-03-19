import json

from fastapi import APIRouter
import requests

social_router = APIRouter(
    prefix="/social",
)


@social_router.get('/')
def all_data():
    data = {'query':
                """
                    query MyQuery {
                      allnamespaces {
                        social {
                          socials {
                            id
                            media
                            name
                            link
                            active
                          }
                        }
                      }
                    }
        
                """}

    headers = {'Content-type': 'application/json'}

    response = requests.post("http://127.0.0.1:8081/graphql", data=json.dumps(data), headers=headers)

    return {'response': response.json()}


