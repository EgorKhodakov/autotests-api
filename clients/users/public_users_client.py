from httpx import Response
from typing import TypedDict
from clients.api_client import ApiClient
from clients.public_http_builder import get_public_http_client


class CreateUserDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class UpdateUserDict(TypedDict):
    """
    Описание структуры запроса для обновления юзера
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class User(TypedDict):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateResponseUser(TypedDict):
    user: User

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


    def create_user(self, request: CreateUserDict) -> CreateResponseUser :
        return self.create_user_api(request).json()

def get_public_users_client() -> PublicUsersClient:
    return PublicUsersClient(client=get_public_http_client())