from utils.User import UserApi


def test_delete_user(api_url, headers):
    # WHEN
    username = UserApi.create(api_url, headers)

    # THEN
    UserApi.delete(api_url, headers, username=username['username'])
    UserApi.get_remote_user_by_username(api_url, headers, username=username['username'])
