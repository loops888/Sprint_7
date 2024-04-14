import allure
import pytest
import requests
import random
import string

import url_constants
from helpers import delete_courier


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@allure.step('Создаем данные для курьера и отпраляем запрос на регистрацию, после чего удаляем его.')
@pytest.fixture
def generate_info_for_courier_and_register():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    yield login_pass

    payload = {
        'login': login,
        'password': password
    }
    login_response = requests.post(url_constants.LOGIN_COURIER, json=payload)
    user_id = login_response.json()['id']
    delete_courier(user_id)

@allure.step('Создаем данные для курьера, передаем их, после чего удаляем его.')
@pytest.fixture
def generate_info_for_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    login_pass.append(login)
    login_pass.append(password)
    login_pass.append(first_name)

    yield login_pass

    payload = {
        'login': login,
        'password': password
    }
    login_response = requests.post(url_constants.LOGIN_COURIER, json=payload)
    user_id = login_response.json()['id']
    delete_courier(user_id)
