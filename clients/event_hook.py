import allure
from httpx import Request, Response
from tools.logger import get_logger
from tools.http.curl import make_curl_from_request

loger = get_logger("HTTP_CLIENT")

def curl_event_hook(request: Request):
    """
    Event hook для автоматического прикрепления cURL команды к Allure отчету.

    :param request: HTTP-запрос, переданный в `httpx` клиент.
    """
    # Генерируем команду cURL из объекта запроса
    curl_command = make_curl_from_request(request)

    # Прикрепляем сгенерированную cURL команду к отчету Allure
    allure.attach(curl_command, "cURL command", allure.attachment_type.TEXT)

def log_request_event_hook(request: Request):
    """
    Логируем информацию от отправленном запросе
    :param request: Обьект запроса HTTPX
    """
    loger.info(f"ake request to {request.url} request method {request.method}")

def log_response_event_hook(response: Response):
    """
    Логируем информацию о полученном ответе
    :param response: Обьект ответа XTTPX
    """
    loger.info(f"Got response {response.status_code} {response.reason_phrase} from {response.url}")