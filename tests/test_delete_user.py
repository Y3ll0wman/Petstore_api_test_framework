from utils.User import UserApi


class TestDeleteUser:
    def test_delete_user(self):
        """Удаляем пользователя"""
        username = UserApi.create()
        UserApi.delete(username=username)
        UserApi.get_remote_user_by_username(username=username)
