from pydantic import BaseModel, Field
from typing import Optional



class BlogPost(BaseModel):
    id: int = Field(ge=0)
    title: str = Field(min_length=5, max_length=100)
    content: str
    published: bool = Field(default=True)
    tags: Optional[list] = []

post_data = {
    "id": 1,
    "title": "My First Post",
    "content": "This is my first post. I'm learning Pydantic!",
    "tags": ["python", "pydantic", "tutorial"]
}

post = BlogPost(**post_data)
print(post)


class User(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: str = Field(min_length=5, max_length=100)
    is_active: bool = Field(default=True)
    roles: list[str] = []
    age: Optional[int]= Field(ge=18, le=120)



user_data = {
    "username": "john_doe",
    "email": "john.doe@example.com",
    "is_active": True,
    "roles": ["admin", "user"],
    "age": 25
}

user = User(**user_data)
print(user)