import httpx
from tools.fakers import random_email
import json


"""Создание пользователя"""


create_user_data = {
  "email": random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_data)
print(json.dumps(create_response.json(), indent=2))

"""Авторизация пользователя"""

login_data = {
    "email": create_user_data["email"],
    "password": create_user_data["password"]
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_data)
print(json.dumps(login_response.json(), indent=2))

"""Загрузка файла"""

auth_token = {
    "Authorization": f"Bearer {login_response.json()['token']['accessToken']}"
    }

create_file_response = httpx.post(
    "http://localhost:8000/api/v1/files", data = {
    "filename": "pantera.png",
    "directory": "courses"},
    files={"upload_file": open("./testdata/files/pantera.png", "rb")},
    headers=auth_token
    )

print(json.dumps(create_file_response.json(), indent=2))