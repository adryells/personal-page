import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse

from api.graphql.schemas import graphql_app
from api.views.random_view import teste

app = FastAPI()
app.add_route('/graphql', graphql_app)
app.include_router(teste)

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*", ],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return HTMLResponse("<a href=http://127.0.0.1:8081/graphql>GRAPHQL</a>")


if __name__ == '__main__':
    uvicorn.run(app, port=8081, host='127.0.0.1')
