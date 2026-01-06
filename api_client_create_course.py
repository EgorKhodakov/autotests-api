from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseSchema
from clients.files.files_client import get_files_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.files.files_schema import  CreateFileRequestShema
from tools.fakers import random_email


"""Создаем Клиента"""

create_user_request = CreateUserRequestSchema(
    email=random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

public_users_client = get_public_users_client()
create_user_response = public_users_client.create_user(create_user_request)
print("Создани клиент: ", create_user_response)


"""Создаем файл"""

auth_request = AuthenticationUserSchema(
    email = create_user_request.email,
    password = create_user_request.password,
)

create_file_request = CreateFileRequestShema(
    filename = "pantera.png",
    directory = "courses",
    upload_file = "./testdata/files/pantera.png"
)

file_client = get_files_client(auth_request)
create_file_response = file_client.create_file(create_file_request)
print("Загружен файл: ", create_file_response)


"""Создаем курс"""

create_course_request = CreateCourseSchema(
    title = "Python Course from Egorka",
    max_score = 100,
    min_score = 10,
    description = "Душим питона",
    estimated_time = "Вся жизнь",
    preview_file_id = create_file_response.file.id,
    created_by_user_id = create_user_response.user.id,
)


course_client = get_courses_client(auth_request)
create_course_response = course_client.create_course(create_course_request)

print("Создан курс: ", create_course_response)