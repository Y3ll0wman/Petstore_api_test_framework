from utils.User import UserApi


def test_user_update(api_url, headers):
    # WHEN
    user_data = UserApi.create(api_url, headers)
    update_user_data = UserApi.user_update(api_url, headers, username=user_data['username'])

    # THEN
    UserApi.get_user_by_username(api_url, headers, username=update_user_data['username'])