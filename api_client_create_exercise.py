
from clients.courses.courses_client import get_courses_client, CreateCourseDict
from clients.exercises.exercises_client import get_exercise_client, CreateExerciseApiDict
from clients.files.files_client import get_files_client, CreateFileDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserDict
from tools.fakers import random_email
import json

"""
Создаем пользователя
"""

create_user_request = CreateUserDict(
    email = random_email(),
    password = "string",
    lastName = "string",
    firstName = "string",
    middleName = "string"
)

public_users_client = get_public_users_client()
create_user_response = public_users_client.create_user(create_user_request)
print("Создан клиент", json.dumps(create_user_response, indent=4))

"""
Инициализируем клиенты для работы с файлами, курсом 2и упражнениями
"""

authentication_user_request = AuthenticationUserDict(
    email = create_user_request["email"],
    password = create_user_request["password"],
)


files_client = get_files_client(authentication_user_request)
course_client = get_courses_client(authentication_user_request)
exercise_client = get_exercise_client(authentication_user_request)

"""
Загружаем файл
"""

create_file_request = CreateFileDict(
    filename = "pantera.png",
    directory = "courses",
    upload_file = "./testdata/files/pantera.png"
)

create_file_response = files_client.create_file(create_file_request)
print("Загружен файл", json.dumps(create_file_response, indent=4))

"""
Создаем курс
"""

create_course_request = CreateCourseDict(
    title="Python Course from Egorka",
    maxScore=100,
    minScore=10,
    description="Trying python",
    estimatedTime="All life",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id'],
)

create_course_response = course_client.create_course(create_course_request)
print("Создан курс", json.dumps(create_course_response, indent=4))

"""
Создаем упражнение
"""

create_exercise_request = CreateExerciseApiDict(
    title = "API Test",
    courseId = create_course_response['course']['id'],
    maxScore = 20,
    minScore = 5,
    orderIndex = 10,
    description = "Trying API",
    estimatedTime = "two days"
)

create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print("Создано упражнение", json.dumps(create_exercise_response, indent=4))