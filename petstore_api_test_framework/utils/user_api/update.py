import allure
import requests
import json

from petstore_api_test_framework.utils import allure_attach
from pydantic import ValidationError
from petstore_api_test_framework.basemodels.user import user_update


def update(api_url, headers, username):
    with allure.step('Обновляем пользователя'):
        method = 'PUT'
        endpoint = f'/v2/user/{username}/'
        try:
            with allure.step('Собираем полезную нагрузку'):
                update_user_request = user_update.UserUpdateRequest.parse_raw(user_update.input_json).json()
                allure_attach.request_body(update_user_request)
                user_data = json.loads(user_update.input_json)

            with allure.step(f'Отправить {method} запрос на {endpoint} для обновления пользователя'):
                response = requests.request(method=method, url=f'{api_url}{endpoint}', headers=headers,
                                            data=update_user_request)
                update_user_response = response.json()
                allure_attach.response_body(update_user_response)

            with allure.step('Проверяем, что API возвращает 200 код ответа'):
                allure_attach.response_code(str(response.status_code))

                assert response.status_code == 200, (f'Update user error. Response code: {response.status_code}'
                                                     f' Response body: {response.json()}')

            with allure.step('Валидация типов данных полученного тела ответа'):
                try:
                    user_update.UserUpdateResponse(
                        code=update_user_response['code'],
                        type=update_user_response['type'],
                        message=update_user_response['message']
                    )

                except ValidationError as e:
                    with allure.step(f'Валидация типов данных не прошла, ошибка: {e}'):
                        raise Exception(f'Валидация типов данных не прошла, ошибка: {e}')

            return user_data

        except requests.ConnectionError as e:
            with allure.step(f'API connection error: {e}'):
                raise Exception(f'API connection error: {e}')
