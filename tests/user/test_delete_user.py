import allure

from petstore_api_test_framework.utils.user_api.create import create
from petstore_api_test_framework.utils.user_api.delete import delete
from petstore_api_test_framework.utils.user_api.get_remote_user_by_username import get_remote_user_by_username


@allure.epic('User API')
@allure.story('Delete user')
@allure.title('Delete user')
@allure.feature('User delete API')
@allure.label('microservice', 'API')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'API', 'normal')
@allure.severity('normal')
def test_delete_user(api_url, headers):
    # WHEN
    username = create(api_url, headers)
    delete(api_url, headers, username=username['username'])

    # THEN
    get_remote_user_by_username(api_url, headers, username=username['username'])
