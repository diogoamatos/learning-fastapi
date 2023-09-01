from fastapi import APIRouter, HTTPException, Query
from typing import Annotated
import schemas
from schemas import fake_items_db, Item


users_router = APIRouter()
items_router = APIRouter()
modelnname_router = APIRouter()
path_param_router = APIRouter()


# Users routes
@users_router.get("/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@users_router.get(
    "/{user_id}",
)
async def read_current_user(user_id: int):
    return {"user_id": user_id}


# Items routes
# Exemplo de query parameters (skip e limit)
@items_router.get("/")
async def read_item(skip: int = 0, limit: int = 100):
    return fake_items_db[skip: skip + limit]


# Utilizando uma Query q como parametro opcional
# Annotated impoe a condição de que quando existir a query q tenha um tamanho
# maximo de 50 caracteres
# para deixar a query q necessaria remove-se o "| None" e "= None"
@items_router.get("/alt")
async def alt_read_item(q: Annotated[str | None, Query(max_length=50)] = None):
    if q:
        return {"data": "retorno com uma query q " + q}
    return fake_items_db


@items_router.get("/{item_id}", tags=["items"])
async def read_items(item_id: int):
    itemInDB = next(
        (item for item in fake_items_db if item["item_id"] == item_id), False)
    if itemInDB:
        return itemInDB
    raise HTTPException(status_code=404, detail=("Item nao encontrado"))


@items_router.put("/{item_id}")
async def update_item(item_id: int, item: Item):
    for i in fake_items_db:
        if i["item_id"] == item_id:
            i["item"] = item
            return i
    return HTTPException(status_code=404, detail="Item não encontrado")


# ModelName -> tests com enumerate
# Os model_names sao extrategias de machine learning
@modelnname_router.get("/{model_name}")
async def read_model_name(model_name: schemas.ModelName):
    if model_name is schemas.ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep learning"}
    if model_name.value == "letnet":
        return {"model_name": model_name, "message": "LcNN?"}
    return {"model_name": model_name, "message": "have some residuals"}


# PATH converter
# O componente :path diz que o parametro deve correnponder com um caminho
# Pode ser necessário um parametro como /home/user/my_file.txt
# Esse sera reprensentado na URL como /files//home/user/my_file.txt
# contendo barras duplas (//) ou (/%2) na URL
@path_param_router.get("/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
