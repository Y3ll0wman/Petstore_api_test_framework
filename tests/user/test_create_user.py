from utils.User import UserApi


class TestCreateUser:
    def test_create_user(self, api_url, headers):
        """Создаем пользователя"""
        username = UserApi.create(api_url, headers)
        UserApi.get_user_by_username(api_url, headers, username=username['username'])
