import allure
import requests

from petstore_api_test_framework.utils import allure_attach
from pydantic import ValidationError
from petstore_api_test_framework.basemodels.user import user_login


def login(api_url, headers, username, password):
    with allure.step('Проходим авторизацию'):
        method = 'GET'
        endpoint = '/v2/user/login/'
        query_params = f'username={username}&password={password}'
        try:
            with allure.step(f'Отправить {method} запрос на {endpoint}?{query_params}'):
                response = requests.request(method=method, url=f'{api_url}{endpoint}?{query_params}', headers=headers)
                user_login_response = response.json()
                allure_attach.response_body(user_login_response)

            with allure.step('Проверяем, что API возвращает 200 код ответа'):
                allure_attach.response_code(str(response.status_code))

                assert response.status_code == 200, (f'User login into the system error. Response code:'
                                                     f'{response.status_code} Response body: {response.json()}')

            with allure.step('Валидация типов данных полученного тела ответа'):
                try:
                    user_login.UserLoginResponse(
                        code=user_login_response['code'],
                        type=user_login_response['type'],
                        message=user_login_response['message']
                    )

                except ValidationError as e:
                    with allure.step(f'Валидация типов данных не прошла, ошибка: {e}'):
                        raise Exception(f'Валидация типов данных не прошла, ошибка: {e}')

            return None

        except requests.ConnectionError as e:
            with allure.step(f'API connection error: {e}'):
                raise Exception(f'API connection error: {e}')
