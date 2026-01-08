from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.private_users_client import  get_private_users_client
from clients.users.users_schema import CreateUserRequestSchema

"""Создание польззователя"""

create_user_request = CreateUserRequestSchema()

public_user_client = get_public_users_client()
create_user_response = public_user_client.create_user(create_user_request)

print(f'Пользователь создан {create_user_response}')


"""Аутентификация пользователя"""

authentication_dict = AuthenticationUserSchema(
    email = create_user_request.email,
    password = create_user_request.password,
)

private_user_client = get_private_users_client(authentication_dict)

auth_user_response = private_user_client.get_user_id(create_user_response.user.id)

print("Получены данные пользователя: ", auth_user_response)



