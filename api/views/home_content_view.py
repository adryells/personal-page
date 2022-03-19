import json

from fastapi import APIRouter
import requests

homecontent_router = APIRouter(
    prefix="/homecontents",
)


@homecontent_router.get('/')
def all_home_contents():
    data = {'query':
                """
                    query MyQuery {
                      allnamespaces {
                        homeContent {
                          homeContents {
                            id
                            homecontenttype
                            content
                            datecreated
                            active
                          }
                        }
                      }
                    }
        
                """}

    headers = {'Content-type': 'application/json'}

    response = requests.post("http://127.0.0.1:8081/graphql", data=json.dumps(data), headers=headers)

    return {'response': response.json()}


