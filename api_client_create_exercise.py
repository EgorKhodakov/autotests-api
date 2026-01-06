
from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseSchema
from clients.exercises.exercises_client import get_exercise_client
from clients.exercises.exercises_schema import CreateExerciseApiSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestShema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import random_email

"""
Создаем пользователя
"""

create_user_request = CreateUserRequestSchema(
    email = random_email(),
    password = "string",
    lastName = "string",
    firstName = "string",
    middleName = "string"
)

public_users_client = get_public_users_client()
create_user_response = public_users_client.create_user(create_user_request)
print("Создан клиент", create_user_response)

"""
Инициализируем клиенты для работы с файлами, курсом 2и упражнениями
"""

authentication_user_request = AuthenticationUserSchema(
    email = create_user_request.email,
    password = create_user_request.password
)


files_client = get_files_client(authentication_user_request)
course_client = get_courses_client(authentication_user_request)
exercise_client = get_exercise_client(authentication_user_request)

"""
Загружаем файл
"""

create_file_request = CreateFileRequestShema(
    filename = "pantera.png",
    directory = "courses",
    upload_file = "./testdata/files/pantera.png"
)

create_file_response = files_client.create_file(create_file_request)
print("Загружен файл", create_file_response)

"""
Создаем курс
"""

create_course_request = CreateCourseSchema(
    title="Python Course from Egorka",
    max_score=100,
    min_score=10,
    description="Trying python",
    estimated_time="All life",
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id,
)

create_course_response = course_client.create_course(create_course_request)
print("Создан курс", create_course_response)

"""
Создаем упражнение
"""

create_exercise_request = CreateExerciseApiSchema(
    title = "API Test",
    course_id = create_course_response.course.id,
    max_score = 20,
    min_score = 5,
    order_index = 10,
    description = "Trying API",
    estimated_time = "two days"
)

create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print("Создано упражнение", create_exercise_response)