import allure
import requests
import json

from petstore_api_test_framework.utils import allure_attach
from pydantic import ValidationError
from petstore_api_test_framework.basemodels.user import user_get_by_username


def get_remote_user_by_username(api_url, headers, username):
    method = 'GET'
    endpoint = '/v2/user'
    """Получаем пользователя по username"""
    try:
        # Отправить GET запрос на /user/{username} для получения пользователя
        response = requests.request('GET', f'{api_url}/v2/user/{username}',
                                    headers=headers)
        get_remote_user_by_username_response_json = response.json()
        # Проверяем, что API возвращает 404 код ответа
        assert response.status_code == 404, f'Get remote user by username error. Response code:' \
                                            f'{response.status_code} Response body: {response.json()}'
        # Валидация типов данных полученного тела ответа
        try:
            user_get_by_username.GetRemoteUserByUsernameResponse(
                code=get_remote_user_by_username_response_json['code'],
                type=get_remote_user_by_username_response_json['type'],
                message=get_remote_user_by_username_response_json['message']
            )
        except ValidationError as e:
            raise e
        print(f'User get by username success. Response body: {response.text} Response code:'
              f'{response.status_code}')
        return None
    except requests.ConnectionError:
        print('API connection error')
