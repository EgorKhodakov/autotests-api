from httpx import Client
from typing import TypedDict
from clients.authentication.authentication_client import get_authentication_client, LoginRequestDict

class AuthenticationUserDict(TypedDict):
    """
    Структура данных пользователя для авторизации
    """
    email: str
    password: str

def get_private_http_client(user: AuthenticationUserDict)-> Client:
    """
    Создает Обьект класса httpx.Client с аутентификацией пользователя
    :param user: email, password
    :return: готовый к испольованию клиент httpx.Client с установленым заголловком для атворизации
    """

    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    login_response = get_authentication_client().login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"authorization": f"Bearer {login_response['token']['accessToken']}"}
    )