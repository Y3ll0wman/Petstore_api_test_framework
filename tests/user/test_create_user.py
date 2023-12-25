from utils.User import UserApi


def test_create_user(api_url, headers):
    username = UserApi.create(api_url, headers)
    UserApi.get_user_by_username(api_url, headers, username=username['username'])
