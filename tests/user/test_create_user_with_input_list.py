from utils.User import UserApi


def test_create_user_with_input_list(api_url, headers):
    UserApi.create_user_with_input_list(api_url, headers)
