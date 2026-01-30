import allure

from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.logger import get_logger

logger = get_logger("ERRORS_ASSERTIONS")

@allure.step("Check validation error")
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Функция для проверки ст структуры ошибка валидации
    :param actual: полученное от API значение
    :param expected: ожидаемое от API значение
    :return: AssertionError если одно хотя бы одно значение не совпадает
    """
    logger.info("Check validation error")

    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.location, expected.location, "location")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")

@allure.step("Check validation error response")
def assert_validation_error_response(actual: ValidationErrorResponseSchema, expected: ValidationErrorResponseSchema):
    """
    Функция проверяющая структуру ответа от API при ошибке валидации
    :param actual: полученный ответ от API
    :param expected: ожидаемый ответ от API
    :return: AssertionError если одно хотя бы одно значение не совпадает
    """
    logger.info("Check validation error response")

    assert_length(actual.details, expected.details, "details")

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)

@allure.step("Check internal error response")
def assert_internal_error_response(actual:InternalErrorResponseSchema, expected: InternalErrorResponseSchema ):
    """
    Функция проверки ответа от апи при внутренней ошибке
    :param actual: полученный от API ответ
    :param expected: ожидаемый от API ответ
    :return: AssertionError если одно хотя бы одно значение не совпадает
    """
    logger.info("Check internal error response")

    assert_equal(actual.details, expected.details, "details")
