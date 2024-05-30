import allure
from api.create_user import UserApi
from api.login_user import LoginUserApi
from data import TestDataUser
import data
from helper import ChangeTestDataHelper
from api.update_user import UpdateUserApi
import pytest
from api.create_order import OrderApi


class TestOrder:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    @allure.description("Генерируем данные, создаем пользователя, делаем логин и делаем заказ с авторизацией. Удаляем пользователя.")
    def test_create_order_with_auth(self, create_creds_user):
        created_user_request = UserApi.create_user(create_creds_user)
        login_user = LoginUserApi.login(create_creds_user)
        create_oder = OrderApi.create_order_with_auth(data.TestDataUser.DATA_FOR_CREATE_ORDER, login_user.json()[
            "accessToken"])
        delete_user_request = UserApi.delete_user(created_user_request.json()[
            "accessToken"])
        assert (create_oder.status_code == 200 and create_oder.json()[
            "success"] == True and delete_user_request.status_code == 202)

    @allure.title("Создание заказа с без авторизации с ингредиентами")
    @allure.description(
        "Делаем заказ без авторизации.")
    def test_create_order_no_auth(self):
        create_oder = OrderApi.create_order_no_auth(data.TestDataUser.DATA_FOR_CREATE_ORDER)
        assert (create_oder.status_code == 200 and create_oder.json()[
            "success"] == True )

    @allure.title("Создание заказа без авторизации без ингредиентов")
    @allure.description(
        "Делаем заказ без авторизации и без ингредиентов.")
    def test_create_order_with_auth_no_ingredients(self):
        create_oder = OrderApi.create_order_no_ingredients()
        assert (create_oder.status_code == 400 and create_oder.text == data.RESPONSE_NO_INGREDIENTS)



    @allure.title("Создание заказа c неверным хешем ингредиента")
    @allure.description(
        "Делаем заказ без авторизации и с неверным хешем.")
    def test_create_order_with_incorrect_hash(self):
        create_oder = OrderApi.create_order_no_auth(data.TestDataUser.INCORRECT_HASH)
        assert (create_oder.status_code == 400 and create_oder.text == data.RESPONSE_INCORRECT_HASH)


