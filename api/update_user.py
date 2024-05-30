import allure
import requests
import data
import urls


class UpdateUserApi:
    @staticmethod
    @allure.step("Обновление данных пользователя с авторизацией")
    def update_info_user_with_auth(update_parametr, access_token):
        return requests.patch(urls.BASE_URL + urls.UPDATE_USER, json=update_parametr,headers={'Authorization': access_token})

    @staticmethod
    @allure.step("Обновление данных пользователя без авторизации")
    def update_info_user_no_auth(update_parametr):
        return requests.patch(urls.BASE_URL + urls.UPDATE_USER, json=update_parametr)