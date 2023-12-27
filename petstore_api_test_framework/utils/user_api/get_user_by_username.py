import allure
import requests
import json

from petstore_api_test_framework.utils import allure_attach
from pydantic import ValidationError
from petstore_api_test_framework.basemodels.user import user_get_by_username


def get_user_by_username(api_url, headers, username):
    method = 'GET'
    endpoint = '/v2/user'
    """Получаем пользователя по username"""
    try:
        # Отправить GET запрос на /user/{username} для получения пользователя
        response = requests.request('GET', f'{api_url}/v2/user/{username}',
                                    headers=headers)
        get_user_by_username_response_json = response.json()
        # Проверяем, что API возвращает 200 код ответа
        assert response.status_code == 200, f'Get user by username error. Response code: {response.status_code}' \
                                            f'Response body: {response.json()}'
        # Валидация типов данных полученного тела ответа
        try:
            user_get_by_username.GetUserByUsernameResponse(
                id=get_user_by_username_response_json['id'],
                username=get_user_by_username_response_json['username'],
                firstName=get_user_by_username_response_json['firstName'],
                lastName=get_user_by_username_response_json['lastName'],
                email=get_user_by_username_response_json['email'],
                password=get_user_by_username_response_json['password'],
                phone=get_user_by_username_response_json['phone'],
                userStatus=get_user_by_username_response_json['userStatus']
            )
        except ValidationError as e:
            raise e
        print(f'User get by username success. Response body: {response.text}. Response code:'
              f'{response.status_code}')
        return None
    except requests.ConnectionError:
        print('API connection error')
