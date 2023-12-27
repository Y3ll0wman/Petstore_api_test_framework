from petstore_api_test_framework.utils.user_api.create import create
from petstore_api_test_framework.utils.user_api.login import login


def test_user_login(api_url, headers):
    # WHEN
    user_data = create(api_url, headers)

    # THEN
    login(api_url, headers, username=user_data['username'], password=user_data['password'])
