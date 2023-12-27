import allure
import requests
import json

from petstore_api_test_framework.utils import allure_attach
from pydantic import ValidationError
from petstore_api_test_framework.basemodels.user import user_create_with_input_array


def create_user_with_input_array(api_url, headers):
    method = 'POST'
    endpoint = '/v2/user/createWithArray'
    """Создаем пользователя"""
    try:
        # Собираем полезную нагрузку
        create_user_with_input_array_request = \
            user_create_with_input_array.CreateUserWithInputArrayRequest.parse_raw(user_create_with_input_array.input_json)
        # Выводим на печать Request body
        print(f'Request body: {user_create_with_input_array.input_json}')
        user_data = json.loads(user_create_with_input_array.input_json)
        # Отправить POST запрос на /user/createWithArray для создания пользователя
        response = requests.request('POST', f'{api_url}/v2/user/createWithArray',
                                    headers=headers, data=create_user_with_input_array_request.json())
        create_user_with_input_array_json = response.json()
        # Проверяем, что API возвращает 200 код ответа
        assert response.status_code == 200, f'User creation with array error.' \
                                            f'Response code: {response.status_code}' \
                                            f'Response body: {response.json()}'
        # Валидация типов данных полученного тела ответа
        try:
            user_create_with_input_array.CreateUserWithInputArrayResponse(
                code=create_user_with_input_array_json['code'],
                type=create_user_with_input_array_json['type'],
                message=create_user_with_input_array_json['message']
            )
        except ValidationError as e:
            raise e
        print(f'User creation with array success. Response body: {response.text}'
              f' Response code: {response.status_code}')
        return user_data
    except requests.ConnectionError:
        print('API connection error')
