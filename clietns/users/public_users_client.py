from httpx import Response
from typing import TypedDict
from clietns.api_client import ApiClient

class CreateUserDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(ApiClient):
    """
    Класс для работы с  /api/v1/users
    """

    def create_user_api(self, request: CreateUserDict) -> Response:
        """
        Метод для создания клиента

        :param request: Словарь я данными для создания полдьзователя
        :return: ответ от сервера в виде обьекта httpx.Response
        """
        return self.post('/api/v1/users', json=request)



