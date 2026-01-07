from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.private_users_client import get_private_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import random_email


"""Создаем пользователя"""

create_user_request = CreateUserRequestSchema(
    email=random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

public_users_client  = get_public_users_client()
create_user_response = public_users_client.create_user(create_user_request)
print(create_user_response)

"""Производим аутентификацию"""

auth_user_request = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password,
)
"""Идентифицируем приватный клиент"""
private_users_client = get_private_users_client(auth_user_request)

"""Выполняем запрос для получения данных о текуущем пользователе"""
get_user_response = private_users_client.get_user_id_api(create_user_response.user.id)

"""Получаем JSON схему модели GetUserResponseSchema"""
get_user_response_schema = GetUserResponseSchema.model_json_schema()

"""Валидируем полученый ответ от API"""
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)





