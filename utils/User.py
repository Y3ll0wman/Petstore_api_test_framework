import requests
from pydantic import ValidationError
from basemodels import UserCreate
from utils.ApiClient import ApiClient


class UserApi:
    @staticmethod
    def create():
        """Создаем пользователя"""
        try:
            # Собираем полезную нагрузку
            create_user_request = UserCreate.CreateUserRequest.parse_raw(UserCreate.input_json)
            # Выводим на печать Request body
            print(f"Request body: {UserCreate.input_json}")
            # Отправить GET запрос на /v2/user для создания пользователя
            response = requests.request("POST", f"{ApiClient.api_url()}/v2/user", headers=ApiClient.headers(),
                                        data=create_user_request.json())
            create_user_response_json = response.json()
            # Проверяем, что API возвращает 200 код ответа
            assert response.status_code == 200, f"User creation error, response code: {response.status_code}," \
                                                f"response body: {response.json()}"
            # Валидация типов данных полученного тела ответа
            try:
                UserCreate.CreateUserResponse(
                    code=create_user_response_json['code'],
                    type=create_user_response_json['type'],
                    message=create_user_response_json['message']
                )
            except ValidationError as e:
                raise e
            print(f'"Response body:", {response.text}, "Response code:", {response.status_code}')
            return response.text
        except requests.ConnectionError:
            print("API connection error")
