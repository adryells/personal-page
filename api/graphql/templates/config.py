from starlette.requests import Request
from starlette.responses import HTMLResponse, Response

from api.graphql.templates.dark import GRAPHQL_HTML


def custom_dark_make_graphiql_handler():
    def handler(request: Request) -> Response:
        return HTMLResponse(GRAPHQL_HTML)

    return handler
