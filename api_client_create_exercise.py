
from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseSchema
from clients.exercises.exercises_client import get_exercise_client
from clients.exercises.exercises_schema import CreateExerciseSchema, UpdateExerciseSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema


"""
Создаем пользователя
"""

create_user_request = CreateUserRequestSchema()

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

create_file_request = CreateFileRequestSchema(
    upload_file = "./testdata/files/pantera.png"
)

create_file_response = files_client.create_file(create_file_request)
print("Загружен файл", create_file_response)

"""
Создаем курс
"""

create_course_request = CreateCourseSchema(
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id,
)

create_course_response = course_client.create_course(create_course_request)
print("Создан курс", create_course_response)

"""
Создаем упражнение
"""

create_exercise_request = CreateExerciseSchema(
    course_id = create_course_response.course.id,
)

create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print("Создано упражнение", create_exercise_response)


"""Обновляем упражнение"""
update_exercise_request = UpdateExerciseSchema()
exercise_id = create_exercise_response["exercise"]["id"]

update_exercise_response = exercise_client.update_exercise(exercise_id, update_exercise_request)

print("Упражнение обновлено", update_exercise_response)