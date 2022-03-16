from enum import Enum

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import HTMLResponse

from api.graphql.schemas import graphql_app
from api.utils.create_database import init_db
from api.utils.populate_db import populate_database

app = FastAPI()
app.add_route('/graphql', graphql_app)


@app.get('/')
async def root():
    return HTMLResponse("<a href=http://127.0.0.1:8081/graphql>GRAPHQL</a>")


@app.on_event("startup")
def on_startup():
    init_db()

    populate_database()


if __name__ == '__main__':
    uvicorn.run(app, port=8081, host='127.0.0.1')
