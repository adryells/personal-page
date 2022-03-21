import json
from typing import List

from fastapi import APIRouter
import requests

blog_router = APIRouter(
    prefix="/blog",
)


@blog_router.get('/')
def all_posts(page: int = None, perpage: int = None, status: bool = None, tags: str = None):
    variables = {
      "page": page,
      "perpage": perpage,
      "status": status,
      "tags": tags.split(',')
    }
    data = {'query':
                """
            query MyQuery ($page: Int, $perpage: Int, $status: Boolean, $tags: [String]){
              allnamespaces {
                post {
                  posts(page: $page, perpage: $perpage, status: $status, tags: $tags) {
                    active
                    content
                    datecreated
                    description
                    englishContent
                    englishDescription
                    englishTitle
                    id
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

    response = requests.post("http://127.0.0.1:8081/graphql", data=json.dumps(data), headers=headers, )

    return {'response': response.json()}


@blog_router.get('/<post_id>')
def get_post(post_id: str):

    variables = {"postId": int(post_id)}

    data = {
        "query":"""
            query MyQuery ($postId: Int){
              allnamespaces{
                post{
                  post(postId: $postId) {
                    active
                    content
                    datecreated
                    description
                    englishContent
                    englishDescription
                    englishTitle
                    id
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
        'variables': variables
    }

    headers = {'Content-type': 'application/json'}

    response = requests.post("http://127.0.0.1:8081/graphql", data=json.dumps(data), headers=headers)

    return {'response': response.json()}