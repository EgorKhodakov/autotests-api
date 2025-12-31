from clients.api_client import ApiClient
from typing import TypedDict
from httpx import Response

from clients.public_http_builder import get_public_http_client


class LoginRequestDict(TypedDict):
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


class LoginResponseDict(TypedDict):
    """
    Описаине структуры ответа ацтентификации
    """
    token: Token


class Token(TypedDict):
    """
    Структура токена аутентификации
    """
    tokenType: str
    accessToken: str
    refreshToken: str


class AuthenticationClient(ApiClient):
    """
    Класс для работы с api/v1/authentication
    """

    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод лля аутентификации пользователя
        :param request: email, password
        :return: обьект типа httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshUserDict) -> Response:
        """
        Метод обновления токена юзера
        :param request: refreshToken
        :return: обьект типа httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        return self.login_api(request).json()

def get_authentication_client() -> AuthenticationClient:
    """
    Создаем клиент атентификации пользователя
    """
    return AuthenticationClient(client=get_public_http_client())


