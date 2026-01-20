from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, FileShema, \
    GetFileResponseSchema
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response


def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Проверка структуры файла
    :param request: параметры запроса переданного в API
    :param response: ответ полученный от API
    :return: AssertionError если одно хотя бы одно значение не совпадает
    """
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"

    assert_equal(response.file.directory, request.directory,"directory")
    assert_equal(response.file.filename, request.filename,"filename")
    assert_equal(str(response.file.url), expected_url, "filename")

def assert_file(actual: FileShema, expected: FileShema):
    """
    Проверка ответа полученного от API при создании файла
    :param actual: Полученный jn API ответ
    :param expected: Ожидаемый от API ответ
    :return: AssertionError если одно хотя бы одно значение не совпадает
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")
    assert_equal(actual.url, expected.url, "filename")

def assert_get_file_response(request: GetFileResponseSchema, response: CreateFileResponseSchema):
    """
    Проверка ответа полученного от API при запросе файла
    :param request: запрос переданный в API
    :param response: ответ полученный от API
    :return: AssertionError если одно хотя бы одно значение не совпадает
    """
    assert_file(request.file, response.file)

def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем соответствует ожидаемой валидационной ошибке
    :param actual: Ответ от API с ошибкой валидации которую необходимо проверить
    :return: AssertionError если одно хотя бы одно значение не совпадает
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                location=["body", "filename"],
                message="String should have at least 1 character",
                input="",
                context={"min_length": 1},
            )
        ]
    )
    assert_validation_error_response(actual, expected)


def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым значением директории соответствует ожидаемой валидационной ошибке
    :param actual: Ответ от API с ошибкой валидации которую необходимо проверить
    :return: AssertionError если одно хотя бы одно значение не совпадает
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                location=["body", "directory"],
                message="String should have at least 1 character",
                input="",
                context={"min_length": 1},
            )
        ]
    )
    assert_validation_error_response(actual, expected)


def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """Проверяет, что ответ на внутреннюю ошибку(например 404) соответствует ожидаемой внутренней ошибке
    :param actual: Ответ от API с внутренней ошибкой которую необходимо проверить
    :return: AssertionError если одно хотя бы одно значение не совпадает
    """
    expected = InternalErrorResponseSchema(details="File not found")
    assert_internal_error_response(actual, expected)


def assert_get_file_with_incorrect_file_id(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на ошибку валидации при некорректном ID в запросе файла соответствует ожидаемой
    валидационой ошибке
    :param actual: Ответ от API с ошибкой валидации которую необходимо проверить
    :return: AssertionError если одно хотя бы одно значение не совпадает
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="uuid_parsing",
                location=["path", "file_id"],
                message="Input should be a valid UUID, invalid character: "
                        "expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                input="incorrect-file-id",
                context={
                    "error": "invalid character: expected an optional prefix "
                             "of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"
                },
            )
        ]
    )

    assert_validation_error_response(actual, expected)

