from httpx import Client
from pydantic import BaseModel, EmailStr
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema
from functools import lru_cache


class AuthenticationUserSchema(BaseModel, frozen=True):
    """
    Структура данных пользователя для авторизации
    """
    email: EmailStr
    password: str


@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationUserSchema)-> Client:
    """
    Создает Обьект класса httpx.Client с аутентификацией пользователя
    :param user: email, password
    :return: готовый к испольованию клиент httpx.Client с установленым заголловком для атворизации
    """

    login_request = LoginRequestSchema(email=user.email,
                                       password=user.password
                                       )
    login_response = get_authentication_client().login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"authorization": f"Bearer {login_response.token.access_token}"},
    )