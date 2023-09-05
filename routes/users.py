from fastapi import APIRouter, Form
from typing import Annotated


users_router = APIRouter()


# Users routes
@users_router.get("/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@users_router.get(
    "/{user_id}",
)
async def read_current_user(user_id: int):
    return {"user_id": user_id}


# A utilizaçao de form é feita por meio de Annotated, tecnicamente o format
# modifica a codificação para multipart/form-data
@users_router.post("/login")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
