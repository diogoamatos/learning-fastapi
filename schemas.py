from enum import Enum
from pydantic import BaseModel


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float


data1 = {
    'name': 'item 1',
    'description': 'primeiro item',
    'price': 13.1
}

data2 = {
    'name': 'item 2',
    'description': 'segundo item',
    'price': 13.1
}

data3 = {
    'name': 'item 3',
    'description': 'terceiro item',
    'price': 13.3
}

fake_items_db = [
    {"item_id": 0, "item": Item(**data1)},
    {"item_id": 1, "item": Item(**data2)},
    {"item_id": 2, "item": Item(**data3)},
]
