from utils.User import UserApi


def test_user_logout(api_url, headers):
    # THEN
    UserApi.user_logout(api_url, headers)
