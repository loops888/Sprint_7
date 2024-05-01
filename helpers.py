import allure

import url_constants
import requests
import random
import string


@allure.step('Генерируем рандомную строку.')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Генерируем данные для регистрации курьера.')
def generate_login_pass_name():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    return login, password, first_name


@allure.step('Отправляем запрос на регистрацию курьера.')
def create_courier(payload):
    request = requests.post(f'{url_constants.URL + url_constants.CREATE_COURIER}', json=payload)
    return request


@allure.step('Отправляем запрос на логин курьера.')
def login_courier(payload):
    request = requests.post(f'{url_constants.URL + url_constants.LOGIN_COURIER}', json=payload)
    return request


@allure.step('Отправляем запрос на удаление курьера.')
def delete_courier(user_id):
    payload = {
        "id": user_id
    }
    request = requests.delete(f'{url_constants.URL + url_constants.DELETE_COURIER}/{user_id}', json=payload)
    return request


@allure.step('Отправляем запрос на создание заказа.')
def create_order(data):
    request = requests.post(f'{url_constants.URL + url_constants.CREATE_ORDER}', json=data)
    return request


@allure.step('Отправляем запрос на получение списка заказов.')
def check_order():
    request = requests.get(f'{url_constants.URL + url_constants.GET_ORDERS_LIST}')
    return request
