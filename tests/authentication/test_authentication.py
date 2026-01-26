from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import PublicUsersClient
from http import HTTPStatus

from fixtures.users import UserFixture
from tools.allure.tags import AllureTag
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.epics import AllureEpic
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
import pytest
import allure


@pytest.mark.regression
@pytest.mark.authentication
@allure.tag(AllureTag.USERS, AllureTag.AUTHENTICATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
class TestAuthentication:

    @allure.title("test login with correct email and password")
    @allure.story(AllureStory.LOGIN)
    def test_login(self, public_users_client: PublicUsersClient,
                   authentication_client: AuthenticationClient,
                   function_user: UserFixture):
        login_user_request = LoginRequestSchema(
            email=function_user.email,
            password=function_user.password
        )

        login_user_response = authentication_client.login_api(login_user_request)
        login_response_data = LoginResponseSchema.model_validate_json(login_user_response.text)

        assert_status_code(login_user_response.status_code, HTTPStatus.OK)
        validate_json_schema(login_user_response.json(), login_response_data.model_json_schema())
        assert_login_response(login_response_data)






