import allure
import requests
import data
import urls


class UserApi:

    @staticmethod
    @allure.step("Отправка запроса на создание пользователя")
    def create_user(body):
        return requests.post(urls.BASE_URL + urls.CREATE_USER, json=body)

    @staticmethod
    @allure.step("Отправка запроса на удаление пользователя")
    def delete_user(user_access_token):
        return requests.delete(urls.BASE_URL + urls.DELETE_USER, headers={'Authorization': user_access_token})