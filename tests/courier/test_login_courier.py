import pytest

import response_constants
from helpers import *


class TestLoginCourier:
    @allure.title('Проверка успешного логина курьера.')
    @allure.description('Если переданы обязательные поля существующего курьера - логин успешен.')
    def test_existed_courier_return_id(self, generate_courier_register_and_delete):
        data = {
            'login': generate_courier_register_and_delete[0],
            'password': generate_courier_register_and_delete[1]
        }
        response = login_courier(data)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверка логина под не существующим пользователем.')
    @allure.description('Если переданы данные по не существующему курьеру - получим ошибку.')
    def test_not_existed_courier_data_not_found(self):
        data = {
            'login': generate_random_string(10),
            'password': generate_random_string(10)
        }
        response = login_courier(data)
        assert response.status_code == 404 and response.json()['message'] == response_constants.NOT_FOUND_MESSAGE

    @allure.title('Проверка логина при отсутствии какого-то поля.')
    @allure.description('Если не переданы обязательные поля login/password - получим ошибку.')
    @pytest.mark.parametrize('data', [({'login': '',
                                        'password': generate_random_string(10)}),
                                      ({'login': generate_random_string(10),
                                        'password': ''})])
    def test_without_necessary_fields_not_found(self, data):
        response = login_courier(data)
        assert response.status_code == 400 and response.json()['message'] == response_constants.NOT_ENOUGH_TO_LOGIN_MESSAGE

    @allure.title('Проверка логина без указания пароля.')
    @allure.description('Если неправильно указан password - получим ошибку.')
    def test_wrong_password_data_not_found(self, generate_courier_register_and_delete):
        data = {
            'login': generate_courier_register_and_delete[0],
            'password': generate_random_string(10)
        }
        response = login_courier(data)
        assert response.status_code == 404 and response.json()['message'] == response_constants.NOT_FOUND_MESSAGE

    @allure.title('Проверка логина без указания пользователя.')
    @allure.description('Если неправильно указан login - получим ошибку.')
    def test_wrong_login_data_not_found(self, generate_courier_register_and_delete):
        data = {
            'login': f'{generate_courier_register_and_delete[0]}{1}',
            'password': generate_courier_register_and_delete[1]
        }
        response = login_courier(data)
        assert response.status_code == 404 and response.json()['message'] == response_constants.NOT_FOUND_MESSAGE
