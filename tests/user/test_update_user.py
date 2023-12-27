from petstore_api_test_framework.utils.user_api.create import create
from petstore_api_test_framework.utils.user_api.update import update
from petstore_api_test_framework.utils.user_api.get_user_by_username import get_user_by_username


def test_update_user(api_url, headers):
    # WHEN
    user_data = create(api_url, headers)
    update_user_data = update(api_url, headers, username=user_data['username'])

    # THEN
    get_user_by_username(api_url, headers, username=update_user_data['username'])
