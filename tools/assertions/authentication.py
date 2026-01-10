from clients.authentication.authentication_schema import LoginResponseSchema
from tools.assertions.base import assert_equal, assert_is_true


def assert_login_response(response: LoginResponseSchema):
    assert_equal(response.token.token_type, "bearer", "Bearer")
    assert_is_true(response.token.access_token, "accessToken")
    assert_is_true(response.token.refresh_token, "refresh_token")