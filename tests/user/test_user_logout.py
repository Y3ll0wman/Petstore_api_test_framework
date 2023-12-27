from petstore_api_test_framework.utils.user_api.logout import logout


def test_user_logout(api_url, headers):
    # THEN
    logout(api_url, headers)
