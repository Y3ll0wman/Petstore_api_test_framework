import allure
import requests

from petstore_api_test_framework.utils import allure_attach
from pydantic import ValidationError
from petstore_api_test_framework.basemodels.user import user_delete


def delete(api_url, headers, username):
    with allure.step('Удаляем пользователя'):
        method = 'DELETE'
        endpoint = f'/v2/user/{username}/'
        try:
            with allure.step(f'Отправить {method} запрос на {endpoint} для удаления пользователя'):
                response = requests.request(method=method, url=f'{api_url}{endpoint}', headers=headers)
                delete_user_response_json = response.json()
                allure_attach.response_body(delete_user_response_json)

            with allure.step('Проверяем, что API возвращает 200 код ответа'):
                allure_attach.response_code(str(response.status_code))

                assert response.status_code == 200, f'User delete error. Response code: {response.status_code}' \
                                                    f'Response body: {response.json()}'

            with allure.step('Валидация типов данных полученного тела ответа'):
                try:
                    user_delete.DeleteUserResponse(
                        code=delete_user_response_json['code'],
                        type=delete_user_response_json['type'],
                        message=delete_user_response_json['message']
                    )

                except ValidationError as e:
                    with allure.step(f'Валидация типов данных не прошла, ошибка: {e}'):
                        raise Exception(f'Валидация типов данных не прошла, ошибка: {e}')

            return None

        except requests.ConnectionError as e:
            with allure.step(f'API connection error: {e}'):
                raise Exception(f'API connection error: {e}')
