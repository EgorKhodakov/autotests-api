import allure

from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema
from tools.assertions.base import assert_equal

@allure.step("Check create user response")
def assert_create_user_response(request:CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Сравнение данных при создании пользователя
    :param request:  Данные от API при запросе
    :param response: Данные от API при ответе
    :return: AssertionError при несовпадении данных
    """
    assert_equal(request.email, response.user.email, "email")
    assert_equal(request.first_name, response.user.first_name, "first_name")
    assert_equal(request.last_name, response.user.last_name, "last_name")
    assert_equal(request.middle_name, response.user.middle_name, "middle_name")

@allure.step("Check user")
def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Функция для сравнения данных двух пользователей
    :param actual: Фактические данные
    :param expected: Ожидаемые данные
    :return: AssertionError при несовпадении данных
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")

@allure.step("Check get user response")
def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    """
    Функция для сравнения данных пользователя полученных от API
    :param get_user_response: данные при запросе пользователя
    :param create_user_response: данные при создании пользователя
    :return: AssertionError при несовпадении данных
    """
    assert_user(get_user_response.user, create_user_response.user)