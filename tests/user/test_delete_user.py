from utils.User import UserApi


class TestDeleteUser:
    def test_delete_user(self, api_url, headers):
        """Удаляем пользователя"""
        username = UserApi.create(api_url, headers)
        UserApi.delete(api_url, headers, username=username['username'])
        UserApi.get_remote_user_by_username(api_url, headers, username=username['username'])
