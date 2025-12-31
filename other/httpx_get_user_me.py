import httpx
import json


"""POST запрос"""

json_data = {
  "email": "user@example.com",
  "password": "string"
}

auth_request = httpx.post('http://localhost:8000/api/v1/authentication/login', json=json_data)
auth_data = auth_request.json()

print("Статус код ответа: от http://localhost:8000/api/v1/authentication/login",auth_request.status_code)
print(json.dumps(auth_request.json(), indent=2))


"""GET запрос"""

headers = {"Authorization": f"Bearer {auth_data['token']['accessToken']}"}

auth_get_request = httpx.get('http://localhost:8000/api/v1/users/me', headers=headers)

print("Статус код ответа: от http://localhost:8000/api/v1/users/me", auth_get_request.json())
print(json.dumps(auth_get_request.json(), indent=2))




