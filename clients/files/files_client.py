from typing import TypedDict
from httpx import Response
from clients.api_client import ApiClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class CreateFileDict(TypedDict):
    """
    Описание структуры запроса для создания файла
    """
    filename: str
    directory: str
    upload_file: str

class File(TypedDict):
    """
    Описание структуры файла
    """
    id: str
    filename: str
    directory: str
    url: str


class CreateFileResponse(TypedDict):
    """
    Описание структуры ответа при создании файла
    """
    file: File

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


    def create_file_api(self, request: CreateFileDict) -> Response:
        """
        Метод для загрузки файла
        :param request: filename, directory, upload_file
        :return:  обьект в виде httpx.Response
        """
        return self.post(
            "/api/v1/files",
            data=request,
            files={"upload_file": open(request['upload_file'], 'rb')}
        )

    def delete_file_api(self, file_id: str ) -> Response:
        """
        Метод для удаления файла
        :param file_id: уникальный идентификатор файла
        :return: обьект в виде httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileDict) -> CreateFileResponse:
        """
         Метод для получения ответа при создании файла
        :param request: filename, directory, upload_file
        :return: возвращает json ответ при создании файла
        """
        return self.create_file_api(request).json()

def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    """
    Создаем клиент для работы с файлами
    """
    return FilesClient(client=get_private_http_client(user))