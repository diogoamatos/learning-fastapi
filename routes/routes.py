from fastapi import APIRouter, HTTPException, Query, Path, Body, Form
from typing import Annotated
import schemas
from schemas import fake_items_db, Item


modelnname_router = APIRouter()


# ModelName -> tests com enumerate
# Os model_names sao extrategias de machine learning
@modelnname_router.get("/{model_name}")
async def read_model_name(model_name: schemas.ModelName):
    if model_name is schemas.ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep learning"}
    if model_name.value == "letnet":
        return {"model_name": model_name, "message": "LcNN?"}
    return {"model_name": model_name, "message": "have some residuals"}
