from pydantic import BaseModel


# Задание 1 Создание базовой модели Pydantic


class Item(BaseModel):

    name: str
    price: int

# Задание 2 Валидация списка объектов
class ItemList(BaseModel):
    items: list[Item]

response = {
  "items": [
    {"name": "Laptop", "price": 1500},
    {"name": "Smartphone", "price": 800}
  ]
}


user_list = ItemList(**response)

print(user_list)