import allure
import requests

from petstore_api_test_framework.utils import allure_attach
from pydantic import ValidationError
from petstore_api_test_framework.basemodels.user import user_logout


def logout(api_url, headers):
    with allure.step('Выйти из системы'):
        method = 'GET'
        endpoint = '/v2/user/logout/'
        try:
            with allure.step(f'Отправить {method} запрос на {endpoint} для выхода из системы'):
                response = requests.request(method='GET', url=f'{api_url}{endpoint}', headers=headers)
                user_logout_response_json = response.json()
                allure_attach.response_body(user_logout_response_json)

            with allure.step('Проверяем, что API возвращает 200 код ответа'):
                allure_attach.response_code(str(response.status_code))

                assert response.status_code == 200, (f'Update user error. Response code: {response.status_code}'
                                                     f' Response body: {response.json()}')

            with allure.step('Валидация типов данных полученного тела ответа'):
                try:
                    user_logout.UserLogOutResponse(
                        code=user_logout_response_json['code'],
                        type=user_logout_response_json['type'],
                        message=user_logout_response_json['message']
                    )

                except ValidationError as e:
                    with allure.step(f'Валидация типов данных не прошла, ошибка: {e}'):
                        raise Exception(f'Валидация типов данных не прошла, ошибка: {e}')

            return None

        except requests.ConnectionError as e:
            with allure.step(f'API connection error: {e}'):
                raise Exception(f'API connection error: {e}')
