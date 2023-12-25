from utils.User import UserApi


def test_create_user_with_input_list(api_url, headers):
    # WHEN
    username = UserApi.create_user_with_input_list(api_url, headers)

    # THEN
    UserApi.get_user_by_username(api_url, headers, username=username[0]['username'])
    UserApi.get_user_by_username(api_url, headers, username=username[1]['username'])