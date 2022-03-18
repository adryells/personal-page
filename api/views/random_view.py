from fastapi import APIRouter

teste = APIRouter(
    prefix="/teste",
)


@teste.get('/')
def que():
    return {}


@teste.get('/acreditas')
def que():
    return {}
