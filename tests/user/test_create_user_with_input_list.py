from petstore_api_test_framework.utils.user_api.create_user_with_input_list import create_user_with_input_list
from petstore_api_test_framework.utils.user_api.get_user_by_username import get_user_by_username


def test_create_user_with_input_list(api_url, headers):
    # WHEN
    username = create_user_with_input_list(api_url, headers)

    # THEN
    get_user_by_username(api_url, headers, username=username[0]['username'])
    get_user_by_username(api_url, headers, username=username[1]['username'])
