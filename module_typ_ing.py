from pydantic import BaseModel, Field
from typing import Optional, List, Tuple, Dict, Literal

from example import response


class UserResponseModel(BaseModel):
    id: int
    name: str
    age: int = Field(ge=18, le=25)
    friends: List[str]
    status: Literal["active", "canceled", "draft"]


user_data = {
    "id": 1,
    "name": "Jog",
    "age": 18,
    "friends": ["Alice", "Bob"],
    "status": "active"
}

user = UserResponseModel(**user_data)


class Product(BaseModel):
    name: str
    price: float = Field(gt=0, le=1000)
    rating: float = Field(ge=1.0, le=5.0)

product = Product(
    name="Laptop",
    price = 599.99,
    rating = 4.5
).model_dump()

Product(**product)

class User(BaseModel):
    username: str = Field(alias="firstName")
    user_status: str = Field(alias="userStatus")

response_server = {
    "id": 150,
    "firstName": "Ivan",
    "userStatus": "active",
    "admin": True

}


User(**response_server)