from fastapi import APIRouter, HTTPException, Query, Path, Body
from typing import Annotated
from schemas import fake_items_db, Item


items_router = APIRouter()


# ---------------------------------------------------------
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


# Do mesmo modo que pode-se declarar parametros de validação,
# pode-se fazer inclusao de metadata ou validacao numeral com o Path,
# como no exemplo em que é declarado o title para item_id
# e esse deve ser maior que 0 (ge=0)
@items_router.get("/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="A ID do item requisitado", ge=0)],
):
    itemInDB = next(
        (item for item in fake_items_db if item["item_id"] == item_id), False
    )
    if itemInDB:
        return itemInDB
    raise HTTPException(status_code=404, detail=("Item nao encontrado"))


# Utilizando Body(embed=True) FastAPI já aguarda um body sem uma chave
# (item no componente 0 da lista fake_items_db) no caso nao e utilizado
# aqui ja que a lista fake_items_db foi criada manualmente e já possui
# a o par chave/valor {"item": Item} e é trocado apenas o valor de Item
@items_router.put("/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    for i in fake_items_db:
        if i["item_id"] == item_id:
            i["item"] = item
            return i
    raise HTTPException(status_code=404, detail="Item não encontrado")
