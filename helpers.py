import allure
import requests
import random
import string
from data import Url


@allure.step(f'Создание пользователя, сохранение данных')
def create_test_user():
    name = generate_string(10)
    password = generate_string(10)
    email = f"{name}@yandex.ru"

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(Url.CREATE_USER, data=payload)

    test_data = {
        "email": email,
        "name": name,
        "password": password,
        "json": response.json()
    }

    return test_data


@allure.step(f'Генерация случайной строки')
def generate_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step(f'Логирование пользователя')
def login_user(email, password):
    payload = {
        "email": email,
        "password": password,
    }

    response = requests.post(Url.LOGIN_USER, data=payload)
    return response


@allure.step(f'Удаление пользователя')
def del_test_user(access_token):
    headers = {'Authorization': access_token}
    requests.delete(Url.AUTH_USER, headers=headers)
