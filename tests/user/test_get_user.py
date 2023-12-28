import allure

from petstore_api_test_framework.utils.user_api.create import create
from petstore_api_test_framework.utils.user_api.get_user_by_username import get_user_by_username


@allure.epic('User API')
@allure.story('Get user')
@allure.title('Get user')
@allure.feature('Get user API')
@allure.label('microservice', 'API')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'API', 'normal')
@allure.severity('normal')
def test_get_user_by_username(api_url, headers):
    # WHEN
    username = create(api_url, headers)

    # THEN
    get_user_by_username(api_url, headers, username=username['username'])
