from httpx import Response
from clients.api_client import ApiClient
from typing import TypedDict

from clients.private_http_builder import get_private_http_client, AuthenticationUserDict

class User(TypedDict):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class GetUserResponseDict(TypedDict):
    user: User


class UpdateUserRequest(TypedDict):
    """
    Описание запроса на обновление пользователя
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class PrivateUsersClient(ApiClient):

    def get_user_me_api(self) -> Response:
        """
        Получение текущего пользователя
        :return: ответ в виде обьекта httpx.Response
        """
        return self.client.get("/api/v1/users/me")

    def get_user_id_api(self, user_id: str) -> Response:
        """
        Получение полььзователя по id
        :param user_id: уникальный идентификатор пользователя
        :return: ответ в виде обьекта httpx.Response
        """
        return self.client.get(f"/api/v1/users/{user_id}")

    def update_user_id_api(self, user_id: str, data: UpdateUserRequest) -> Response:
        """
        Метод частичного обновления пользователя
        :param user_id: уникальный идентификатор пользователя
        :param data: email, lastName, firstName, middleName
        :return: ответ в виде обьекта httpx.Response
        """
        return self.client.patch(f"/api/v1/users/{user_id}", data=data)

    def delete_user_id_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя
        :param user_id: уникальный идентификатор пользователя
        :return: ответ в виде обьекта httpx.Response
        """
        return self.client.delete(f"/api/v1/users/{user_id}")


    def get_user_id(self, user_id: str) -> GetUserResponseDict:
        """
        Метод для получения авторизационных данных пользователя
        :param user_id: уникальный идентификатор пользователя
        :return: авторизационные данные пользователя в формате json
        """
        return self.get_user_id_api(user_id).json()



def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
    """
    Создаем клиент для работы с юзерами
    """
    return PrivateUsersClient(client=get_private_http_client(user))