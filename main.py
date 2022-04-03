import uvicorn
import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse

from api.graphql.schemas import graphql_app
from api.views import views

app = FastAPI()
app.add_route('/graphql', graphql_app)

STATIC_DIR = os.path.join(os.path.dirname(__file__), "frontend/static")
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "frontend/templates")

for route in views:
    app.include_router(route)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*", ],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root():
    return HTMLResponse("<a href=http://localhost:5000/graphql>GRAPHQL</a>")


if __name__ == '__main__':
    uvicorn.run(app, port=5000, host='0.0.0.0')
