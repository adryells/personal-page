import json

from fastapi import APIRouter
import requests

data_router = APIRouter(
    prefix="/data",
)


@data_router.get('/')
def all_data():
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
                social {
                  socials {
                    id
                    media
                    name
                    link
                    active
                  }
                }
                tag {
                  tags {
                    id
                    portugueseName
                    englishName
                    active
                  }
                }
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


