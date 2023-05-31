from utils.User import UserApi


class TestCreateUserWithInputList:
    def test_create_user_with_input_list(self):
        """Создаем пользователя"""
        UserApi.create_user_with_input_list()
