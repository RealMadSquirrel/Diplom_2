import allure
from api.create_user import UserApi
from api.login_user import LoginUserApi
from data import TestDataUser
import data
from helper import ChangeTestDataHelper
from api.update_user import UpdateUserApi
import pytest
from api.get_orders import GetOrder


class TestGetOrder:
    @allure.title("Запрос списка заказов с авторизацией")
    @allure.description("Генерируем данные, создаем пользователя, делаем логин и запрашиваем заказы с авторизацией. Удаляем пользователя.")
    def test_get_order_with_auth(self, create_and_delete_user):
        login_user = LoginUserApi.login(create_and_delete_user)
        get_oder = GetOrder.get_order_with_auth(login_user.json()["accessToken"])
        assert get_oder.status_code == 200 and get_oder.json()[
            "success"] == True

    @allure.title("Запрос списка заказов без авторизации")
    @allure.description("Делаем запрос и получаем ошибку 401.")
    def test_get_order_no_auth(self):
        get_oder = GetOrder.get_order_no_auth()
        assert (get_oder.status_code == 401 and get_oder.json()[
            "success"] == False)