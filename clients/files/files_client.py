from typing import TypedDict
from httpx import Response
from clients.api_client import ApiClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.files.files_schema import CreateFileRequestShema, CreateFileResponseShema


class FilesClient(ApiClient):
    """
    Клиент для рабтоы с /api/v1/files
    """

    def get_file_api(self, file_id: str ) -> Response:
        """
        Метод для получения файла
        :param file_id: уникальный идентификатор файла
        :return: обьект в виде httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")


    def create_file_api(self, request: CreateFileRequestShema) -> Response:
        """
        Метод для загрузки файла
        :param request: filename, directory, upload_file
        :return:  обьект в виде httpx.Response
        """
        return self.post(
            "/api/v1/files",
            data=request.model_dump(by_alias=True, exclude={'upload_file'}),
            files={"upload_file": open(request.upload_file, 'rb')}
        )

    def delete_file_api(self, file_id: str ) -> Response:
        """
        Метод для удаления файла
        :param file_id: уникальный идентификатор файла
        :return: обьект в виде httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestShema) -> CreateFileResponseShema:
        """
         Метод для получения ответа при создании файла
        :param request: filename, directory, upload_file
        :return: возвращает json ответ при создании файла
        """
        responce = self.create_file_api(request)
        return CreateFileResponseShema.model_validate_json(responce.text)

def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    Создаем клиент для работы с файлами
    """
    return FilesClient(client=get_private_http_client(user))