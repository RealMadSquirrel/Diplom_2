import pytest
import helper
from helper import UserFactory
import allure
from api.create_user import UserApi

@allure.step("Генерация кред для пользователя, создание рандомного пользователя и удаление")
@pytest.fixture(scope='function')
def create_and_delete_user():
    creds = helper.UserFactory.register_new_user_and_return_load()
    created_user_request = UserApi.create_user(creds)
    yield creds
    UserApi.delete_user(created_user_request.json()[
                            "accessToken"])

@allure.step("Генерация кред для пользователя")
@pytest.fixture(scope='function')
def create_creds_user():
    creds = helper.UserFactory.register_new_user_and_return_load()
    yield creds





