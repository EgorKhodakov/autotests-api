import httpx
import json
from tools.fakers import fake, random_password

"""Создание пользователя"""

create_user_data = {
  "email": fake.email(),
  "password": random_password(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

response_create_user = httpx.post("http://localhost:8000/api/v1/users", json=create_user_data)

print("Код ответа:", response_create_user.status_code)
print("Создан пользователь с данными:", json.dumps(response_create_user.json(), indent=2))

"""Авторизация пользователя"""

auth_user_data = {
  "email":create_user_data['email'],
  "password":create_user_data['password'],
}

auth_user_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=auth_user_data)

print("Код ответа:", auth_user_response.status_code)
print("Авторизован пользователь:", json.dumps(auth_user_response.json(), indent=2))

"""Обновление пользователя"""

update_user_data = {
  "email": fake.email(),
  "lastName": create_user_data['lastName'],
  "firstName": create_user_data['firstName'],
  "middleName": create_user_data['middleName']
}

update_user_headers = {
    "Authorization": f"Bearer {auth_user_response.json()['token']['accessToken']}",
}

update_response_user = httpx.patch(
    f"http://localhost:8000/api/v1/users/{response_create_user.json()['user']['id']}",
    json=update_user_data,
    headers=update_user_headers
)

print("Код ответа:", update_response_user.status_code)
print("Данные пользователя изменены на:", json.dumps(update_response_user.json(), indent=2 ))
