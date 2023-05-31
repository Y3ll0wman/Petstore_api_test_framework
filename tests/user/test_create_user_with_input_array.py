from utils.User import UserApi


class TestCreateUserWithInputArray:
    def test_create_user_with_input_array(self):
        """Создаем пользователя"""
        UserApi.create_user_with_input_array()
