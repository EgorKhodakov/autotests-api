import allure
from httpx import Client, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles
from typing import Any

class ApiClient:
    def __init__(self, client: Client):
        """
        Базовый API клиент, принимающий обьект httpx.Client
        :param client:экземпляр httpx.Client для выполнения HTTP-запросов
        """
        self.client = client

    @allure.step("Make GET request to {url}")
    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Запрос для получения данных

        :param url: URL адрес эндпоинта
        :param params: query параметры запроса
        :return: обьект Response с данными ответа
        """
        return self.client.get(url, params=params)

    @allure.step("Make POST request to {url}")
    def post(self,
             url: URL | str,
             data: RequestData | None = None,
             json: Any | None = None,
             files: RequestFiles | None = None,
             ) -> Response:
        """
        Выполняет POST-запрос.

        ::param url: URL-адрес эндпоинта.
        :param json: Данные в формате JSON.
        :param data: Форматированные данные формы (например, application/x-www-form-urlencoded).
        :param files: Файлы для загрузки на сервер.
        :return: Объект Response с данными ответа.
        """
        return self.client.post(url, data=data, json=json, files=files)

    @allure.step("Make PATCH request to {url}")
    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Выполняет PATCH-запрос (частичное обновление данных).

        :param url: URL-адрес эндпоинта.
        :param json: Данные для обновления в формате JSON.
        :return: Объект Response с данными ответа.
        """
        return self.client.patch(url=url, json=json)

    @allure.step("Make DELETE request to {url}")
    def delete(self, url: URL | str) -> Response:
        """
        Выполняет DELETE-запрос (удаление данных).

        :param url: URL-адрес эндпоинта.
        :return: Объект Response с данными ответа.
        """
        return self.client.delete(url)



