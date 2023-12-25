from utils.User import UserApi


def test_get_user_by_username(api_url, headers):
    # WHEN
    username = UserApi.create(api_url, headers)

    # THEN
    UserApi.get_user_by_username(api_url, headers, username=username['username'])
