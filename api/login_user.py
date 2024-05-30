import allure
import requests
import data
import urls


class LoginUserApi:
    @staticmethod
    @allure.step("Авторизация пользователя")
    def login(creds):
        return requests.post(urls.BASE_URL + urls.LOGIN, json=creds)