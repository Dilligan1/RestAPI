from pydantic import BaseModel, TypeAdapter
from typing import Optional


class Post(BaseModel):
    id: int
    content: str


class MainModel(BaseModel):

    id: int
    status: str
    tags: list[str]
    posts: dict[str, Post]


response = {
    "id": 1234,
    "status": "active",
    "tags": ["music", "people", "greeting"],
    "posts": {
        "post_1": {
            "id": 56,
            "content": "I'm sick"
        },
        "post_2": {
            "id": 46,
            "content": "I'm good"
        }
    }
}


user = MainModel(**response)



class UserModel(BaseModel):
    name: str
    last_name: str
    admin: Optional[bool] = False

adapter = TypeAdapter(list(MainModel))

response = [
    {
        "name": "Aleksei",
        "last_name": "Dobro",
        "admin": True
    },
    {
        "name": "Ivan",
        "last_name": "Zlo"
    }
]

adapter = adapter.validate_python(response)