from utils.User import UserApi


class TestUserLogin:
    def test_user_login(self):
        user_data = UserApi.create()
        UserApi.user_login(username=user_data['username'], password=user_data['password'])
