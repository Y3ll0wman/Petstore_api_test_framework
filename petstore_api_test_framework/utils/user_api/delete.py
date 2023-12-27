import allure
import requests

from petstore_api_test_framework.utils import allure_attach
from pydantic import ValidationError
from petstore_api_test_framework.basemodels.user import user_delete


def delete(api_url, headers, username):
    method = 'DELETE'
    endpoint = '/v2/user'
    """Удаляем пользователя"""
    try:
        # Отправить DELETE запрос на /user/{username} для удаления пользователя
        response = requests.request('DELETE', f'{api_url}/v2/user/{username}',
                                    headers=headers)
        delete_user_response_json = response.json()
        # Проверяем, что API возвращает 200 код ответа
        assert response.status_code == 200, f'User delete error. Response code: {response.status_code}' \
                                            f'Response body: {response.json()}'
        # Валидация типов данных полученного тела ответа
        try:
            user_delete.DeleteUserResponse(
                code=delete_user_response_json['code'],
                type=delete_user_response_json['type'],
                message=delete_user_response_json['message']
            )
        except ValidationError as e:
            raise e
        print(f'User delete success. Response body: {response.text} Response code: {response.status_code}')
        return None
    except requests.ConnectionError:
        print('API connection error')
