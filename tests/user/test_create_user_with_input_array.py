from utils.User import UserApi


class TestCreateUserWithInputArray:
    def test_create_user_with_input_array(self, api_url, headers):
        """Создаем пользователя"""
        UserApi.create_user_with_input_array(api_url, headers)
