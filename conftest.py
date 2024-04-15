import pytest
from helpers import *


@allure.step('Создаем данные для курьера, передаем их, после чего удаляем его.')
@pytest.fixture
def generate_courier_and_delete():
    data = generate_login_pass_name()

    login_pass = [data[0], data[1], data[2]]

    yield login_pass

    payload = {
        'login': data[0],
        'password': data[1]
    }
    login_response = login_courier(payload)
    user_id = login_response.json()['id']
    delete_courier(user_id)


@allure.step('Создаем данные для курьера, регистрируем его, после чего удаляем.')
@pytest.fixture
def generate_courier_register_and_delete():
    data = generate_login_pass_name()
    payload = {
        "login": data[0],
        "password": data[1],
        "firstName": data[2]
    }
    registration_response = create_courier(payload)
    login_pass = []
    if registration_response.status_code == 201:
        login_pass.append(data[0])
        login_pass.append(data[1])
        login_pass.append(data[2])

    yield login_pass

    payload = {
        'login': data[0],
        'password': data[1]
    }
    login_response = login_courier(payload)
    user_id = login_response.json()['id']
    delete_courier(user_id)
