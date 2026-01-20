from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length


def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Функция для проверки ст структуры ошибка валидации
    :param actual: полученное от API значение
    :param expected: ожидаемое от API значение
    :return: AssertionError если одно хотя бы одно значение не совпадает
    """
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.location, expected.location, "location")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")


def assert_validation_error_response(actual: ValidationErrorResponseSchema, expected: ValidationErrorResponseSchema):
    """
    Функция проверяющая структуру ответа от API при ошибке валидации
    :param actual: полученный ответ от API
    :param expected: ожидаемый ответ от API
    :return: AssertionError если одно хотя бы одно значение не совпадает
    """
    assert_length(actual.details, expected.details, "details")

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)

def assert_internal_error_response(actual:InternalErrorResponseSchema, expected: InternalErrorResponseSchema ):
    """
    Функция проверки ответа от апи при внутренней ошибке
    :param actual: полученный от API ответ
    :param expected: ожидаемый от API ответ
    :return: AssertionError если одно хотя бы одно значение не совпадает
    """
    assert_equal(actual.details, expected.details, "details")
