import allure
from httpx import Response
from clients.api_client import ApiClient
from clients.users.users_schema import GetUserResponseSchema, UpdateUserRequestSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class PrivateUsersClient(ApiClient):

    @allure.step("Get user me")
    def get_user_me_api(self) -> Response:
        """
        Получение текущего пользователя
        :return: ответ в виде обьекта httpx.Response
        """
        return self.get("/api/v1/users/me")

    @allure.step("Get user by id {user_id}")
    def get_user_id_api(self, user_id: str) -> Response:
        """
        Получение полььзователя по id
        :param user_id: уникальный идентификатор пользователя
        :return: ответ в виде обьекта httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    @allure.step("Update user {user_id}")
    def update_user_id_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод частичного обновления пользователя
        :param user_id: уникальный идентификатор пользователя
        :param request: email, lastName, firstName, middleName
        :return: ответ в виде обьекта httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete user {user_id}")
    def delete_user_id_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя
        :param user_id: уникальный идентификатор пользователя
        :return: ответ в виде обьекта httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user_id(self, user_id: str) -> GetUserResponseSchema:
        """
        Метод для получения авторизационных данных пользователя
        :param user_id: уникальный идентификатор пользователя
        :return: авторизационные данные пользователя в формате json
        """
        response = self.get_user_id_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)



def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Создаем клиент для работы с юзерами
    """
    return PrivateUsersClient(client=get_private_http_client(user))