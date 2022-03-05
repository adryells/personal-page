import uvicorn
from fastapi import FastAPI

from api.graphql.schemas import graphql_app
from api.utils.create_database import init_db
from api.utils.populate_db import populate_database

app = FastAPI()
app.add_route('/graphql', graphql_app)


@app.get('/')
async def graphql():
    return {"message": "hello"}


@app.on_event("startup")
def on_startup():
    init_db()

    populate_database()


if __name__ == '__main__':
    uvicorn.run(app, port=8081, host='127.0.0.1')
