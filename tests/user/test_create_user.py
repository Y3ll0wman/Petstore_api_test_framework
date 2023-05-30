from utils.User import UserApi


class TestCreateUser:
    def test_create_user(self):
        """Создаем пользователя"""
        username = UserApi.create()
        UserApi.get_user_by_username(username=username['username'])
