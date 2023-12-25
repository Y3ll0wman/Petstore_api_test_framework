from utils.User import UserApi


def test_user_login(api_url, headers):
    # WHEN
    user_data = UserApi.create(api_url, headers)

    # THEN
    UserApi.user_login(api_url, headers, username=user_data['username'], password=user_data['password'])
