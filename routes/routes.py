from fastapi import APIRouter, HTTPException, Query, Path, Body, Form
from typing import Annotated
import schemas
from schemas import fake_items_db, Item


modelnname_router = APIRouter()
path_param_router = APIRouter()


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
