from fastapi import APIRouter, HTTPException
import schemas

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


fake_items_db = [
    {"item_id": 0, "item_name": "foo"},
    {"item_id": 1, "item_name": "bar"},
    {"item_id": 2, "item_name": "foobar"},
]


# Items routes
@items_router.get("/")
async def read_item(skip: int = 0, limit: int = 100):
    return fake_items_db[skip: skip + limit]


@items_router.get("/{item_id}", tags=["items"])
async def read_items(item_id: int):
    item = next((item for item in fake_items_db if item["item_id"] == item_id), False)
    if item:
        return item
    raise HTTPException(status_code=404, detail=("Item nao encontrado"))


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
