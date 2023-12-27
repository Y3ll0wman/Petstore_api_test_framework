from petstore_api_test_framework.utils.user_api.create import create
from petstore_api_test_framework.utils.user_api.get_user_by_username import get_user_by_username


def test_get_user_by_username(api_url, headers):
    # WHEN
    username = create(api_url, headers)

    # THEN
    get_user_by_username(api_url, headers, username=username['username'])
