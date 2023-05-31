from utils.User import UserApi


class TestUserLogout:
    def test_user_logout(self):
        UserApi.user_logout()
