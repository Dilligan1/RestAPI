from pydantic import BaseModel, field_validator
from datetime import date


class User(BaseModel):
    name: str
    age: int
    date: date

    @field_validator("date")
    def check_not_data(cls, value):
        if value < date.today():
            raise  ValueError("Дата не может быть в прошлом")
        return value



response = {
    "name": "Ilya",
    "age": 24,
    "date": "2025-11-17"
}

User(**response)


class Logs(BaseModel):
    id: int
    log: str

    @field_validator("log")
    def logs_has_correct_data(cls, value):
        if "error" in value:
            raise ValueError("Найдены ошибки в логах")
        return

response = {
    "id": 1,
    "log": "This is log with error"
}
Logs(**response)