from enum import Enum
from pydantic import BaseModel, Field, HttpUrl


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# Pydantic valida strings de URL automaticamente com HttpUrl
class Image(BaseModel):
    url: HttpUrl
    name: str


# Assim como Query e Path, Field adiciona validaçao e metadata dentro dos
# modelos do pydantic
class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="a descricao do item", max_length=300
    )
    price: float = Field(gt=0, description="o preco deve ser maior que zero")
    # pode-se utilizar modelos pydantic como subtipos por meio de list
    # (python3.10+) e caso seja necessario que os items sejam unicos
    # (se for tags por exemplo) é só utilizar:
    tags: set[str] = set()
    # images: list[Image] | None = None

    # Pode-se declarar exeplos para o Pydantic incluir no schema JSON
    # da documentacao utilizando model_config ou os exemplos podem ser
    # declarados inline de cada variavel exemplo:
    # name: str = Field(examples=["Foo"])
    # description: str | None = Field(default=None, examples=["Um item bem maneiro"]
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    'name': 'Foo',
                    'description': 'Um item bem maneiro',
                    'price': 13.1
                }
            ]
        }
    }


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
