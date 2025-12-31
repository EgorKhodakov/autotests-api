from clients.courses.courses_client import get_courses_client, CreateCourseDict
from clients.files.files_client import get_files_client, CreateFileDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserDict
from tools.fakers import random_email
import json


"""Создаем Клиента"""

create_user_request = CreateUserDict(
    email = random_email(),
    password = "string",
    lastName = "string",
    firstName = "string",
    middleName = "string"
)

public_users_client = get_public_users_client()
create_user_response = public_users_client.create_user(create_user_request)
print("Создани клиент: ", json.dumps(create_user_response, indent=4))


"""Создаем файл"""

auth_data = AuthenticationUserDict(
    email = create_user_request['email'],
    password = create_user_request['password'],
)

create_file_request = CreateFileDict(
    filename = "pantera.png",
    directory = "courses",
    upload_file = "./testdata/files/pantera.png"
)

file_client = get_files_client(auth_data)
create_file_response = file_client.create_file(create_file_request)
print("Загружен файл: ", json.dumps(create_file_response, indent=4))


"""Создаем курс"""

create_course_request = CreateCourseDict(
    title = "Python Course from Egorka",
    maxScore = 100,
    minScore = 10,
    description = "Душим питона",
    estimatedTime = "Вся жизнь",
    previewFileId = create_file_response['file']['id'],
    createdByUserId = create_user_response['user']['id'],
)


course_client = get_courses_client(auth_data)
create_course_response = course_client.create_course(create_course_request)

print("Создан курс: ", json.dumps(create_course_response, indent=4))