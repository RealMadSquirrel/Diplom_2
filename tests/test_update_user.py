import allure
from api.create_user import UserApi
from api.login_user import LoginUserApi
from data import TestDataUser
import data
from helper import ChangeTestDataHelper
from api.update_user import UpdateUserApi
import pytest


class TestUpdateUser:
    @allure.title("Проверка обновления параметров пользователя c авторизацией - Успешное обновление")
    @allure.description("Генерируем данные для создания пользователя, создаем пользователя, делаем логин и пытаемся изменить каждый параметр. Удаляем пользователя.")
    @pytest.mark.parametrize('key, value', data.TestDataUser.DATA_UPDATE)
    def test_success_update_user_with_auth(self, create_and_delete_user, key, value):
        login_user = LoginUserApi.login(create_and_delete_user)
        update_user = UpdateUserApi.update_info_user_with_auth(ChangeTestDataHelper.modify_payload_body(data.TestDataUser.UPDATE_JSON, key, value), login_user.json()[
            "accessToken"])
        assert update_user.status_code == 200 and update_user.json()["success"] == True



    @allure.title("Проверка обновления параметров пользователя без авторизации")
    @allure.description(
        "Генерируем данные для создания пользователя, создаем пользователя и без авторизации пытаемся изменить каждый параметр. Удаляем пользователя.")
    @pytest.mark.parametrize('key, value', data.TestDataUser.DATA_UPDATE)
    def test_update_user_no_auth(self, create_and_delete_user, key, value):
        login_user = LoginUserApi.login(create_and_delete_user)
        update_user = UpdateUserApi.update_info_user_no_auth(
            ChangeTestDataHelper.modify_payload_body(data.TestDataUser.UPDATE_JSON, key, value))
        assert update_user.status_code == 401 and update_user.json()["success"] == False