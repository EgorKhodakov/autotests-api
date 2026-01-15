import pytest
from pydantic import BaseModel, EmailStr
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    """
    Модель для агрегации возвращаемых данных фикстурой function_user
    """
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self):
        """
        доступ к email пользователя
        """
        return self.request.email

    @property
    def password(self):
        """
        доступ к паролю пользователя
        """
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        """
        доступ к email и паролю для аутентификации
        """
        return AuthenticationUserSchema(
            email=self.request.email,
            password=self.request.password
        )


@pytest.fixture
def public_users_client() ->PublicUsersClient:
    """
    Инициализация публичного клиента
    """
    return get_public_users_client()


@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    """
    Фикстура для создания пользователя
    """
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)

@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    """
    Инициализация приватного клиент
    """
    return get_private_users_client(function_user.authentication_user)



