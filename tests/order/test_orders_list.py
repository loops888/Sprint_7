import allure

from helpers import check_order


class TestOrdersList:
    @allure.title('Проверка получения списка заказов.')
    @allure.description(
        'Если отправить запрос на список заказов без указания конкретного заказа - вернется весь список заказов.')
    def test_no_specific_order_get_all_created_orders(self):
        response = check_order()
        assert response.status_code == 200 and 'orders' in response.text
