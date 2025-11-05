import requests
from faker import Faker

faker = Faker()



# Получить всех персонажей "Rick and Morty"
def get_all_characters():
    response = requests.get(
        url="https://rickandmortyapi.com/api/character")
    if response.status_code == 200:
        data = response.json()["results"]
        for character in data:
            print(character["name"])
    else:
        print("Ошибка при получении данных:", response.status_code)



# Найти всех персонажей с именем "Rick"

def find_characters_by_name(character_name: str):
    response = requests.get(
        url= "https://rickandmortyapi.com/api/character",
        params= {
            "name": character_name,
        }
    )
    if response.status_code == 200:
        print(f"Количество персонажей с именем {character_name}:", len(response.json()))
    else:
        print(f"Персонаж с заданным именем: {character_name} отсутствует")




# Создание юзера
def create_user(name: str, job: str):
    response =  requests.post(
        headers= {
            "x-api-key": "reqres-free-v1"
        },
        url="https://reqres.in/api/users",
        json= {
            "name": name,
            "job": job
        })
    if response.status_code == 201:
        print(response.json())
    else:
        print("Пользователи не созданы")

create_user(name=faker.name(), job=faker.job())


def update_user_job(user_id: str, new_job: str):
    response = requests.patch(
        headers= {"x-api-key": "reqres-free-v1"},
        url= "https://reqres.in/api/users/2",
        json= {"name": user_id, "job": new_job}

    )
    if response.status_code == 200:
        print(response.json())
        assert response.json()["job"] == new_job
    else:
        print("Ошибка в обновлении данных")

update_user_job("Gabriel Conway", "124")


def delete_user(user_id: int):
    try:
        response = requests.delete(
            url=f"https://reqres.in/api/users/{user_id}",
            headers={"x-api-key": "reqres-free-v1"},
        )
        assert response.status_code == 204, "Пользователь не удален"
        print(f"Пользователь с {user_id} удален статус код:", response.status_code)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

delete_user(2)
