import pytest
import helper
from helper import UserFactory
import allure


@allure.step("Создание рандомного пользователя")
@pytest.fixture(scope='function')
def create_creds_user():
    creds = helper.UserFactory.register_new_user_and_return_load()
    return creds


