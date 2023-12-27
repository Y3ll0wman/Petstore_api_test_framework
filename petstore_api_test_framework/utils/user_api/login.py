import allure
import requests
import json

from petstore_api_test_framework.utils import allure_attach
from pydantic import ValidationError
from petstore_api_test_framework.basemodels.user import user_login


def login(api_url, headers, username, password):
    method = 'GET'
    endpoint = '/v2/user/login'
    query_params = f'username={username}&password={password}'
    """Проходим авторизацию в систему"""
    try:
        # Отправить GET запрос на /user/login?username={username}&password={password}
        response = requests.request('GET',
                                    f'{api_url}/v2/user/login?username={username}&password={password}',
                                    headers=headers)
        user_login_response = response.json()
        # Проверяем, что API возвращает 200 код ответа
        assert response.status_code == 200, (f'User login into the system error. Response code:'
                                             f'{response.status_code} Response body: {response.json()}')
        # Валидация типов данных полученного тела ответа
        try:
            user_login.UserLoginResponse(
                code=user_login_response['code'],
                type=user_login_response['type'],
                message=user_login_response['message']
            )
        except ValidationError as e:
            raise e
        print(f'User login success. Response body: {response.text} Response code: {response.status_code}')
        return None
    except requests.ConnectionError:
        print('API connection error')
