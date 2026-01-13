from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema
from http import HTTPStatus

from tests.conftest import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
import pytest


@pytest.mark.regression
@pytest.mark.authentication
def test_login(public_users_client: PublicUsersClient,
               authentication_client: AuthenticationClient,
               function_user: UserFixture,):

    """Логинимся"""

    login_user_request = LoginRequestSchema(
        email=function_user.email,
        password=function_user.password
    )

    login_user_response = authentication_client.login_api(login_user_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_user_response.text)

    """Производим проверки"""
    assert_status_code(login_user_response.status_code, HTTPStatus.OK)
    validate_json_schema(login_user_response.json(), login_response_data.model_json_schema())
    assert_login_response(login_response_data)






