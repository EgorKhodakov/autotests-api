import allure
from httpx import Response
from clients.api_client import ApiClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(ApiClient):
    """
    Класс для работы с  /api/v1/users
    """

    @allure.step("Create User")
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод запроса для создания клиента

        :param request: Словарь я данными для создания полдьзователя
        :return: ответ от сервера в виде обьекта httpx.Response
        """
        return self.post('/api/v1/users', json=request.model_dump(by_alias=True))


    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)

def get_public_users_client() -> PublicUsersClient:
    return PublicUsersClient(client=get_public_http_client())