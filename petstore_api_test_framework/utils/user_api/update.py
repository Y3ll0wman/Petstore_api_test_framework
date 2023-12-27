import allure
import requests
import json

from petstore_api_test_framework.utils import allure_attach
from pydantic import ValidationError
from petstore_api_test_framework.basemodels.user import user_update


def update(api_url, headers, username):
    method = 'PUT'
    endpoint = f'/v2/user/{username}'
    """Обновляем пользователя"""
    try:
        # Собираем полезную нагрузку
        update_user_request = user_update.UserUpdateRequest.parse_raw(user_update.input_json)
        # Выводим на печать Request body
        print(f"Request body: {user_update.input_json}")
        user_data = json.loads(user_update.input_json)
        # Отправить PUT запрос на /user/{username}
        response = requests.request('PUT', f'{api_url}/v2/user/{username}', headers=headers,
                                    data=update_user_request.json())
        update_user_response = response.json()
        # Проверяем, что API возвращает 200 код ответа
        assert response.status_code == 200, (f'Update user error. Response code: {response.status_code}'
                                             f' Response body: {response.json()}')
        # Валидация типов данных полученного тела ответа
        try:
            user_update.UserUpdateResponse(
                code=update_user_response['code'],
                type=update_user_response['type'],
                message=update_user_response['message']
            )
        except ValidationError as e:
            raise e
        print(f'Update user success. Response body: {response.text} Response code: {response.status_code}')
        return user_data
    except requests.ConnectionError:
        print('API connection error')
