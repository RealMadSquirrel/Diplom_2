import allure
import requests
import data
import urls


class GetOrder:

    @staticmethod
    @allure.step("Запрос заказов пользователя с авторизацией")
    def get_order_with_auth(user_access_token):
        return requests.get(urls.BASE_URL + urls.GET_ORDERS, headers={'Authorization': user_access_token})

    @staticmethod
    @allure.step("Запрос заказов без авторизации")
    def get_order_no_auth():
        return requests.get(urls.BASE_URL + urls.GET_ORDERS)