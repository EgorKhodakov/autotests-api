from http import HTTPStatus

import allure
import pytest

from clients.errors_schema import ValidationErrorResponseSchema, InternalErrorResponseSchema
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from fixtures.files import FilesFixture
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_create_file_response, assert_get_file_response, \
    assert_create_file_with_empty_filename_response, assert_create_file_with_empty_directory_response, \
    assert_file_not_found_response, assert_get_file_with_incorrect_file_id
from tools.assertions.schema import validate_json_schema



@pytest.mark.regression
@pytest.mark.files
class TestFiles:

    @allure.title("test create file")
    def test_create_file(self, files_client: FilesClient, ):
        request = CreateFileRequestSchema(upload_file="./testdata/files/pantera.png")
        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_create_file_response(request, response_data)

    @allure.title("test get file")
    def test_get_file(self, files_client: FilesClient, function_file: FilesFixture):
        response = files_client.get_file_api(function_file.response.file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_file_response(response_data, function_file.response)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("test create file with empty filename")
    def test_create_file_with_empty_filename(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            upload_file="./testdata/files/pantera.png",
            filename=""
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_CONTENT)
        assert_create_file_with_empty_filename_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("test create file with empty directory")
    def test_create_file_with_empty_directory(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            upload_file="./testdata/files/pantera.png",
            directory=""
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_CONTENT)
        assert_create_file_with_empty_directory_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("test delete file")
    def test_delete_file(self, files_client: FilesClient, function_file: FilesFixture):
        delete_response = files_client.delete_file_api(function_file.response.file.id)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = files_client.get_file_api(function_file.response.file.id)
        get_response_data =InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        validate_json_schema(get_response.json(), get_response_data.model_json_schema())
        assert_file_not_found_response(get_response_data)

    @allure.title("test get file with incorrect file id")
    def test_get_file_with_incorrect_file_id(self, files_client: FilesClient, function_file: FilesFixture):
        response = files_client.get_file_api(file_id="incorrect-file-id")
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_CONTENT)
        assert_get_file_with_incorrect_file_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())
