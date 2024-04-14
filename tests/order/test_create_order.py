import allure
import pytest
from generators import Data
from helpers import create_order


class TestCreateOrder:
    @allure.title('Проверка создания заказа.')
    @allure.description('Вне зависимости от значения поля color - заказ создается успешно и возвращается track.')
    @pytest.mark.parametrize('data', [
        ({
            'firstName': Data.first_name,
            'lastName': Data.last_name,
            'address': Data.address,
            'metroStation': Data.metro_station,
            'phone': Data.phone_number,
            'rentTime': Data.rent_time,
            'deliveryDate': Data.delivery_date,
            'comment': Data.comment,
            'color': ["BLACK"]}),
        ({
            'firstName': Data.first_name,
            'lastName': Data.last_name,
            'address': Data.address,
            'metroStation': Data.metro_station,
            'phone': Data.phone_number,
            'rentTime': Data.rent_time,
            'deliveryDate': Data.delivery_date,
            'comment': Data.comment,
            'color': ["GREY"]}),
        ({
            'firstName': Data.first_name,
            'lastName': Data.last_name,
            'address': Data.address,
            'metroStation': Data.metro_station,
            'phone': Data.phone_number,
            'rentTime': Data.rent_time,
            'deliveryDate': Data.delivery_date,
            'comment': Data.comment,
            'color': ["BLACK", "GREY"]}),
        ({
            'firstName': Data.first_name,
            'lastName': Data.last_name,
            'address': Data.address,
            'metroStation': Data.metro_station,
            'phone': Data.phone_number,
            'rentTime': Data.rent_time,
            'deliveryDate': Data.delivery_date,
            'comment': Data.comment})
    ])
    def test_order_creation_get_track(self, data):
        response = create_order(data)
        assert response.status_code == 201 and 'track' in response.text
