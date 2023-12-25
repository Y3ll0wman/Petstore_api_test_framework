from utils.User import UserApi


def test_user_update(api_url, headers):
    user_data = UserApi.create(api_url, headers)
    UserApi.user_update(api_url, headers, username=user_data['username'])
