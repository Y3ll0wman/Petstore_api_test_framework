from utils.User import UserApi
import pytest


class TestCreateUser:
    @pytest.mark.xfail
    def test_user_update(self):
        """Создаем пользователя"""
        user_data = UserApi.create()
        updated_user_data = UserApi.user_update(username=user_data['username'])
        UserApi.get_user_by_username(username=updated_user_data['username'])
