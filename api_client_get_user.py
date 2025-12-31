from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserDict
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from tools.fakers import random_email
import json

"""Создание польззователя"""

create_user_data = CreateUserDict(
    email = random_email(),
    password = "string",
    lastName = "string",
    firstName =  "string",
    middleName = "string"
)

public_user_client = get_public_users_client()
create_user_response = public_user_client.create_user(create_user_data)

print(f'Пользователь создан {json.dumps(create_user_response, indent=2)}')


"""Аутентификация пользователя"""

authentication_dict = AuthenticationUserDict(
    email = create_user_data["email"],
    password = create_user_data["password"],
)

private_user_client = get_private_users_client(authentication_dict)

auth_user_response = private_user_client.get_user_id(create_user_response['user']['id'])

print("Получены данные пользователя: ", json.dumps(auth_user_response, indent=2))



