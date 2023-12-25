from utils.User import UserApi


class TestCreateUser:
    def test_user_update(self):
        """Создаем пользователя"""
        user_data = UserApi.create()
        UserApi.user_update(username=user_data['username'])
