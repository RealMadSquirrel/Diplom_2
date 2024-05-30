import allure
from api.create_user import UserApi
from api.login_user import LoginUserApi
import data
from helper import ChangeTestDataHelper


class TestLoginUser:
    @allure.title("Проверка авторизации созданного пользователя")
    @allure.description("Генерируем данные для создания пользователя, создаем пользователя, проверяем логин")
    def test_success_login_user(self, create_creds_user):
        created_user_request = UserApi.create_user(create_creds_user)
        login_user = LoginUserApi.login(create_creds_user)
        delete_user_request = UserApi.delete_user(login_user.json()[
            "accessToken"])
        assert (login_user.status_code == 200 and login_user.json()[
            "success"] == True and delete_user_request.status_code == 202)

    @allure.title("Проверка авторизации созданного пользователя с неверным паролем")
    @allure.description("Генерируем данные для создания пользователя, создаем пользователя, проверяем логин с неверным паролем")
    def test_login_user_incorrect_password(self, create_creds_user):
        created_user_request = UserApi.create_user(create_creds_user)
        login_user = LoginUserApi.login(ChangeTestDataHelper.modify_payload_body(create_creds_user,'password','123'))
        delete_user_request = UserApi.delete_user(created_user_request.json()[
                                                      "accessToken"])
        assert (login_user.status_code == 401 and login_user.json()[
            "success"] == False and delete_user_request.status_code == 202)