import allure
import requests
import json

from petstore_api_test_framework.utils import allure_attach
from pydantic import ValidationError
from petstore_api_test_framework.basemodels.user import user_logout


def logout(api_url, headers):
    method = 'GET'
    endpoint = '/v2/user/logout'
    """Выйти из системы"""
    try:
        # Отправить GET запрос на /user/logout
        response = requests.request('GET', f'{api_url}/v2/user/logout', headers=headers)
        user_logout_response = response.json()
        # Проверяем, что API возвращает 200 код ответа
        assert response.status_code == 200, (f'Update user error. Response code: {response.status_code}'
                                             f' Response body: {response.json()}')
        # Валидация типов данных полученного тела ответа
        try:
            user_logout.UserLogOutResponse(
                code=user_logout_response['code'],
                type=user_logout_response['type'],
                message=user_logout_response['message']
            )
        except ValidationError as e:
            raise e
        print(f'User logout success. Response body: {response.text} Response code: {response.status_code}')
        return None
    except requests.ConnectionError:
        print('API connection error')
