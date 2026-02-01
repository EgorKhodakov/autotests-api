import allure
from httpx import Response
from clients.api_client import ApiClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from tools.routes import APIRoutes


class FilesClient(ApiClient):
    """
    Клиент для работы с /api/v1/files
    """

    @allure.step("Get file by id {file_id}")
    def get_file_api(self, file_id: str ) -> Response:
        """
        Метод для получения файла
        :param file_id: уникальный идентификатор файла
        :return: обьект в виде httpx.Response
        """
        return self.get(f"{APIRoutes.FILES}/{file_id}")

    @allure.step("Create file")
    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Метод для загрузки файла
        :param request: filename, directory, upload_file
        :return:  обьект в виде httpx.Response
        """
        return self.post(
            APIRoutes.FILES,
            data=request.model_dump(by_alias=True, exclude={'upload_file'}),
            files={"upload_file": request.upload_file.read_bytes()}
        )

    @allure.step("Delete File {file_id}")
    def delete_file_api(self, file_id: str ) -> Response:
        """
        Метод для удаления файла
        :param file_id: уникальный идентификатор файла
        :return: обьект в виде httpx.Response
        """
        return self.delete(f"{APIRoutes.FILES}/{file_id}")

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        """
         Метод для получения ответа при создании файла
        :param request: filename, directory, upload_file
        :return: возвращает json ответ при создании файла
        """
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)

def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    Создаем клиент для работы с файлами
    """
    return FilesClient(client=get_private_http_client(user))