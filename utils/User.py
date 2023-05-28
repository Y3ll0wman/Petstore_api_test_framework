import requests
from pydantic import ValidationError
from basemodels import UserCreate
from utils.ApiClient import ApiClient


class UserApi:
    @staticmethod
    def create():
        """Создаем пользователя"""
        try:
            # Собираем полезную нагрузку и заголовки для запроса на API эндпоинт
            create_user_request = UserCreate.CreateUserRequest.parse_raw(UserCreate.input_json)
            print(f"Request body: {UserCreate.input_json}")
            j = create_user_request.json()
            url = f"{ApiClient.api_url()}/v2/user"
            payload = j
            headers = ApiClient.headers()
            # Отправить GET запрос на /v2/user для создания пользователя
            response = requests.request("POST", url, headers=headers, data=payload)
            create_user_response_json = response.json()
            # Проверяем, что API возвращает 200 код ответа
            assert response.status_code == 200, f"User creation error, response code: {response.status_code}," \
                                                f"response body: {response.json()}"
            # Проверяем типы данных в полученном теле ответа
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
