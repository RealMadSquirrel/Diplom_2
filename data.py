import pytest
import urls


class TestDataUser:
    UPDATE_JSON = {
            "param": "param"
        }

    DATA_UPDATE = [['email','testgj@gmail.com'],['password','123456'],['name','Olga']]

    DATA_FOR_CREATE_ORDER = {
"ingredients": ["61c0c5a71d1f82001bdaaa6d","609646e4dc916e00276b2871"]
}

    INCORRECT_HASH = {
"ingredients": ["61c0c5a71d1f82001bdaaa65"]
}




SUCCESS_CREATE_USER = '{"ok":true}'
EMPTY_USER = 'Недостаточно данных для создания учетной записи'
LOGIN_EMPTY_USER = 'Недостаточно данных для входа'
LOGIN_NONEXISTENT_USER = 'Учетная запись не найдена'
EMPTY_PARAM = 'Email, password and name are required fields'
DOUBLE_USER = 'User already exists'
RESPONSE_NO_INGREDIENTS = '{"success":false,"message":"Ingredient ids must be provided"}'
RESPONSE_INCORRECT_HASH = '{"success":false,"message":"One or more ids provided are incorrect"}'