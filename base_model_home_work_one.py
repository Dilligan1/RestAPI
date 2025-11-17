from pydantic import BaseModel, Field, field_validator
from typing import List
from datetime import date

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





class Item(BaseModel):
    name: str
    price: float = Field(gt=0)  # цена должна быть больше 0

class Order(BaseModel):
    customer_name: str = Field(min_length=1)
    order_date: date
    items: List[Item]

    @field_validator("order_date")
    def check_in_data_today(cls, value):
        if value < date.today():
            raise ValueError("Дата в прошлом")
        return value


# Пример данных
order_data = {
    "customer_name": "Alex",
    "order_date": "2023-12-31",
    "items": [
        {"name": "Laptop", "price": 1500},
        {"name": "Smartphone", "price": 800}
    ]
}


order = Order(**order_data)
print(order)
