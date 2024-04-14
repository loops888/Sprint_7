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


@allure.step('Отправляем запрос на регистрацию курьера.')
def create_courier(data):
    request = requests.post(url_constants.CREATE_COURIER, json=data)
    return request


@allure.step('Отправляем запрос на логин курьера.')
def login_courier(data):
    request = requests.post(url_constants.LOGIN_COURIER, json=data)
    return request


@allure.step('Отправляем запрос на удаление курьера.')
def delete_courier(user_id):
    payload = {
        "id": user_id
    }
    request = requests.delete(f'{url_constants.DELETE_COURIER}/{user_id}', json=payload)
    return request


@allure.step('Отправляем запрос на создание заказа.')
def create_order(data):
    request = requests.post(url_constants.CREATE_ORDER, json=data)
    return request


@allure.step('Отправляем запрос на получение списка заказов.')
def check_order():
    request = requests.get(url_constants.GET_ORDERS_LIST)
    return request
