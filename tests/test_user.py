import allure
from api.create_user import UserApi
import data
from helper import ChangeTestDataHelper


class TestCreateUser:
    @allure.title("Проверка успешности создания пользователя")
    @allure.description("Создание шаблонного пользователя, проверка статуса ответа и тела ответа")
    def test_success_create_user(self, create_creds_user):
        created_user_request = UserApi.create_user(create_creds_user)
        delete_user_request = UserApi.delete_user(created_user_request.json()[
            "accessToken"])
        assert (created_user_request.status_code == 200 and created_user_request.json()[
            "success"] == True and delete_user_request.status_code == 202)

    @allure.title("Проверка невозможности создать двух одинаковых пользователей")
    @allure.description("Запоминаем креды. Создаем user и пытаемся создать user с такими же кредами.")
    def test_create_user_duplicate(self, create_creds_user):
        UserApi.create_user(create_creds_user)
        created_user_request_2 = UserApi.create_user(create_creds_user)
        assert (created_user_request_2.status_code == 403 and created_user_request_2.json()[
            "message"] == data.DOUBLE_USER)

    @allure.title("Проверка, что нельзя создать пользователя с незаполненным email.")
    @allure.description("Проверка, что нельзя создать курьера с пустыми данными.")
    def test_create_user_with_empty_email(self, create_creds_user):
        create_creds_user_new = ChangeTestDataHelper.modify_payload_body(create_creds_user,'email','')
        created_user_request = UserApi.create_user(create_creds_user_new)
        assert (created_user_request.status_code == 403 and created_user_request.json()["message"] == data.EMPTY_PARAM)
