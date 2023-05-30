from utils.User import UserApi


class TestDeleteUser:
    def test_delete_user(self):
        """Получаем пользователя по username"""
        username = UserApi.create()
        UserApi.get_user_by_username(username=username['username'])
