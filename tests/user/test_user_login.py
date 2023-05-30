from utils.User import UserApi


class TestUserLogin:
    def test_user_login(self):
        user = UserApi.create()
        UserApi.user_login(username=user['username'], password=user['password'])
