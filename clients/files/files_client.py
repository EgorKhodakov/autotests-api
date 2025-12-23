from typing import TypedDict
from httpx import Response
from clients.api_client import ApiClient

class CreateFileDict(TypedDict):
    """
    Описание структуры запроса для создания файла
    """
    filename: str
    directory: str
    upload_file: str


class FilesClient(ApiClient):
    """
    Клиент для рабтоы с /api/v1/files
    """

    def get_file(self, file_id: str ) -> Response:
        """
        Метод для получения файла
        :param file_id: уникальный идентификатор файла
        :return: обьект в виде httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")


    def create_file(self, request: CreateFileDict) -> Response:
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

    def delete_file(self, file_id: str ) -> Response:
        """
        Метод для удаления файла
        :param file_id: уникальный идентификатор файла
        :return: обьект в виде httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")