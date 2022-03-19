import json

from fastapi import APIRouter
import requests

blog_router = APIRouter(
    prefix="/blog",
)


@blog_router.get('/')
def all_posts():
    data = {'query':
                """
                    query MyQuery {
                      allnamespaces {
                        post {
                          posts {
                            id
                            title
                            media
                            englishTitle
                            englishDescription
                            englishContent
                            description
                            datecreated
                            active
                            content
                          }
                        }
                      }
                    }
        
                """}

    headers = {'Content-type': 'application/json'}

    response = requests.post("http://127.0.0.1:8081/graphql", data=json.dumps(data), headers=headers)

    return {'response': response.json()}