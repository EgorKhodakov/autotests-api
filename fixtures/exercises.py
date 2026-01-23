import pytest
from pydantic import BaseModel
from clients.exercises.exercises_client import ExercisesClient, get_exercise_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CoursesFixture
from fixtures.users import UserFixture


class ExersiceFixture(BaseModel):
    """
    Модель для агрегации возвращенных данных фикстурой function_exercise
    """
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    """
    инициализация клиента ExercisesClient
    :param function_user:
    :return:
    """
    return get_exercise_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(exercises_client : ExercisesClient, function_course: CoursesFixture) -> ExersiceFixture:
    """
    Создание упражнения
    """
    request = CreateExerciseRequestSchema(
        courseId=function_course.response.course.id
    )
    response = exercises_client.create_exercise(request)
    return ExersiceFixture(
        request=request,
        response=response,
    )

