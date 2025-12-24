from clients.api_client import ApiClient
from typing import TypedDict
from httpx import Response


class AuthenticationUserDict(TypedDict):
    """
    Структура запроса для аутентификации пользователя
    """
    email: str
    password: str


class RefreshUserDict(TypedDict):
    """
    Структура запроса для обновления токена
    """
    refreshToken: str

class AuthenticationUser(ApiClient):
    """
    Класс для работы с api/v1/authentication
    """

    def login_user_api(self, request: AuthenticationUserDict) -> Response:
        """
        Метод лля аутентификации пользователя
        :param request: email, password
        :return: обьект типа httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_user_api(self, request: RefreshUserDict) -> Response:
        """
        Метод обновления токена юзера
        :param request: refreshToken
        :return: обьект типа httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)


