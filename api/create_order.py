import allure
import requests
import data
import urls


class OrderApi:

    @staticmethod
    @allure.step("Отправка запроса на создание заказа с авторизацией")
    def create_order_with_auth(body,user_access_token):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER, json=body, headers={'Authorization': user_access_token} )

    @staticmethod
    @allure.step("Отправка запроса на создание заказа без авторизации")
    def create_order_no_auth(body):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER, json=body)

    @staticmethod
    @allure.step("Отправка запроса на создание заказа без ингредиентов")
    def create_order_no_ingredients():
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER)

