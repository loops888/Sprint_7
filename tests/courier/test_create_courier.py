import allure
import pytest

import response_constants
from helpers import generate_random_string, create_courier


class TestCreateCourier:
    @allure.title('Проверка успешной регистрации курьера.')
    @allure.description('Если переданы корректные данные для регистрации - курьер создается успешно.')
    def test_random_data_new_courier_created(self, generate_info_for_courier):
        data = {
            'login': generate_info_for_courier[0],
            'password': generate_info_for_courier[1],
            'name': generate_info_for_courier[2]
        }
        response = create_courier(data)
        assert response.status_code == 201 and response.json() == response_constants.SUCCESSFUL_REQUEST

    @allure.title('Проверка повторной регистрации существующего курьера.')
    @allure.description('Если переданы дубли при регистрации - получим ошибку.')
    def test_existing_user_conflict(self, generate_info_for_courier_and_register):
        data = {
            'login': generate_info_for_courier_and_register[0],
            'password': generate_info_for_courier_and_register[1],
            'firstName': generate_info_for_courier_and_register[2]
        }
        response = create_courier(data)
        assert response.status_code == 409 and response.json()['message'] == response_constants.CONFLICT_MESSAGE

    @allure.title('Проверка регистрации без обязательных полей.')
    @allure.description('Если не переданы обязательные поля login/password при регистрации - получим ошибку.')
    @pytest.mark.parametrize('data', [({'password': generate_random_string(10),
                                        'name': generate_random_string(10)}),
                                      ({'login': generate_random_string(10),
                                        'name': generate_random_string(10)}),
                                      ({'name': generate_random_string(10)})])
    def test_without_login_and_password_not_enough_data(self, data):
        response = create_courier(data)
        assert response.status_code == 400 and response.json()['message'] == response_constants.NOT_ENOUGH_TO_CREATE_MESSAGE
