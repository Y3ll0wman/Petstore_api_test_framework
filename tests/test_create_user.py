from utils.User import UserApi


class TestCreateUser:
    def test_create_user(self):
        """Создаем пользователя"""
        UserApi.create()
