from httpx import Client

def get_public_http_client()->Client:
    """
    Функция создает экс=земпляр класса httpx.Client с базовыми настройками
    :return: готовый к использованию обьект httpx.Client
    """
    return Client(timeout=100, base_url="http://localhost:8000")