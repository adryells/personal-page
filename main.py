import uvicorn
from fastapi import FastAPI


from api.graphql.schemas import graphql_app

app = FastAPI()
app.add_route('/graphql', graphql_app)


@app.get('/')
async def graphql():
    return {"message": "hello"}


if __name__ == '__main__':
    uvicorn.run(app, port=8081, host='127.0.0.1')
