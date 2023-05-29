import requests
import json
from pydantic import ValidationError
from basemodels import UserCreate, UserDelete
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
            username = json.loads(UserCreate.input_json)['username']
            # Отправить POST запрос на /v2/user для создания пользователя
            response = requests.request("POST", f"{ApiClient.api_url()}/user", headers=ApiClient.headers(),
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
            print(f'User creation success. Response body:, {response.text}, Response code:, {response.status_code}')
            return username
        except requests.ConnectionError:
            print("API connection error")

    @staticmethod
    def delete(username):
        """Удаляем пользователя"""
        try:
            # Отправить DELETE запрос на /user/{username} для удаления пользователя
            response = requests.request("DELETE", f"{ApiClient.api_url()}/user/{username}",
                                        headers=ApiClient.headers())
            delete_user_response_json = response.json()
            # Проверяем, что API возвращает 200 код ответа
            assert response.status_code == 200, f"User delete error, response code: {response.status_code}," \
                                                f"response body: {response.json()}"
            # Валидация типов данных полученного тела ответа
            try:
                UserDelete.DeleteUserResponse(
                    code=delete_user_response_json['code'],
                    type=delete_user_response_json['type'],
                    message=delete_user_response_json['message']
                )
            except ValidationError as e:
                raise e
            print(f'User delete success. Response body, {response.text}. Response code:, {response.status_code}')
            return response.text
        except requests.ConnectionError:
            print("API connection error")
