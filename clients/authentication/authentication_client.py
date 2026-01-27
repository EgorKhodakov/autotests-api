import allure

from clients.api_client import ApiClient
from httpx import Response

from clients.public_http_builder import get_public_http_client
from clients.authentication.authentication_schema import LoginRequestSchema, RefreshRequestSchema, LoginResponseSchema



class AuthenticationClient(ApiClient):
    """
    Класс для работы с api/v1/authentication
    """

    @allure.step("Authenticate user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод для аутентификации пользователя
        :param request: email, password
        :return: обьект типа httpx.Response
        """
        return self.post(
            "/api/v1/authentication/login",
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Refresh authentication token")
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Метод обновления токена юзера
        :param request: refreshToken
        :return: обьект типа httpx.Response
        """
        return self.post(
            "/api/v1/authentication/refresh",
            json=request.model_dump(by_alias=True)
        )

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)

def get_authentication_client() -> AuthenticationClient:
    """
    Создаем клиент атентификации пользователя
    """
    return AuthenticationClient(client=get_public_http_client())


