import requests
import json
from pydantic import ValidationError
from basemodels.User import UserCreate, UserDelete, UserGetByUsername, UserLogin
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
            username = json.loads(UserCreate.input_json)
            # Отправить POST запрос на /v2/user для создания пользователя
            response = requests.request("POST", f"{ApiClient.api_url()}/user", headers=ApiClient.headers(),
                                        data=create_user_request.json())
            create_user_response_json = response.json()
            # Проверяем, что API возвращает 200 код ответа
            assert response.status_code == 200, f"User creation error. Response code: {response.status_code}." \
                                                f"Response body: {response.json()}"
            # Валидация типов данных полученного тела ответа
            try:
                UserCreate.CreateUserResponse(
                    code=create_user_response_json['code'],
                    type=create_user_response_json['type'],
                    message=create_user_response_json['message']
                )
            except ValidationError as e:
                raise e
            print(f'User creation success. Response body: {response.text} Response code: {response.status_code}')
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
            assert response.status_code == 200, f"User delete error. Response code: {response.status_code}" \
                                                f"Response body: {response.json()}"
            # Валидация типов данных полученного тела ответа
            try:
                UserDelete.DeleteUserResponse(
                    code=delete_user_response_json['code'],
                    type=delete_user_response_json['type'],
                    message=delete_user_response_json['message']
                )
            except ValidationError as e:
                raise e
            print(f'User delete success. Response body: {response.text} Response code: {response.status_code}')
            return None
        except requests.ConnectionError:
            print("API connection error")

    @staticmethod
    def get_user_by_username(username):
        """Получаем пользователя по username"""
        try:
            # Отправить GET запрос на /user/{username} для получения пользователя
            response = requests.request("GET", f"{ApiClient.api_url()}/user/{username}",
                                        headers=ApiClient.headers())
            get_user_by_username_response_json = response.json()
            # Проверяем, что API возвращает 200 код ответа
            assert response.status_code == 200, f"Get user by username error. Response code: {response.status_code}" \
                                                f"Response body: {response.json()}"
            # Валидация типов данных полученного тела ответа
            try:
                UserGetByUsername.GetUserByUsernameResponse(
                    id=get_user_by_username_response_json['id'],
                    username=get_user_by_username_response_json['username'],
                    firstName=get_user_by_username_response_json['firstName'],
                    lastName=get_user_by_username_response_json['lastName'],
                    email=get_user_by_username_response_json['email'],
                    password=get_user_by_username_response_json['password'],
                    phone=get_user_by_username_response_json['phone'],
                    userStatus=get_user_by_username_response_json['userStatus']
                )
            except ValidationError as e:
                raise e
            print(f'User get by username success. Response body: {response.text}. Response code:'
                  f'{response.status_code}')
            return None
        except requests.ConnectionError:
            print("API connection error")

    @staticmethod
    def get_remote_user_by_username(username):
        """Получаем пользователя по username"""
        try:
            # Отправить GET запрос на /user/{username} для получения пользователя
            response = requests.request("GET", f"{ApiClient.api_url()}/user/{username}",
                                        headers=ApiClient.headers())
            get_remote_user_by_username_response_json = response.json()
            # Проверяем, что API возвращает 404 код ответа
            assert response.status_code == 404, f"Get remote user by username error. Response code:" \
                                                f"{response.status_code} Response body: {response.json()}"
            # Валидация типов данных полученного тела ответа
            try:
                UserGetByUsername.GetRemoteUserByUsernameResponse(
                    code=get_remote_user_by_username_response_json['code'],
                    type=get_remote_user_by_username_response_json['type'],
                    message=get_remote_user_by_username_response_json['message']
                )
            except ValidationError as e:
                raise e
            print(f'User get by username success. Response body: {response.text} Response code:'
                  f'{response.status_code}')
            return None
        except requests.ConnectionError:
            print("API connection error")

    @staticmethod
    def user_login(username, password):
        """Проходим авторизацию в систему"""
        try:
            # Отправить GET запрос на /user/login?username={username}&password={password}
            response = requests.request("GET",
                                        f"{ApiClient.api_url()}/user/login?username={username}&password={password}",
                                        headers=ApiClient.headers())
            user_login_response = response.json()
            # Проверяем, что API возвращает 200 код ответа
            assert response.status_code == 200, (f'User login into the system error. Response code:'
                                                 f'{response.status_code} Response body: {response.json()}')
            # Валидация типов данных полученного тела ответа
            try:
                UserLogin.CreateUserResponse(
                    code=user_login_response['code'],
                    type=user_login_response['type'],
                    message=user_login_response['message']
                )
            except ValidationError as e:
                raise e
            print(f'User login success. Response body: {response.text} Response code: {response.status_code}')
            return None
        except requests.ConnectionError:
            print("API connection error")
