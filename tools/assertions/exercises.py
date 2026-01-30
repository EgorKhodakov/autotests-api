from typing import List
import allure
from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    ExerciseSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExercisesResponseSchema, \
    GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.logger import get_logger

logger = get_logger("EXERCISE_ASSERTIONS")

@allure.step("Check create exercise response")
def assert_create_exercise_response(actual: CreateExerciseResponseSchema, expected: CreateExerciseRequestSchema):
    """
    Проверяет что созданное упражнение соответствует ожидаемом модели данных
    :param actual: ответ полученный от API который нужно проверить
    :param expected: запрос переданный в API
    :return: AssertionError если хотя бы одно значение не совпадает
    """
    logger.info("Check create exercise response")

    assert_equal(actual.exercise.title, expected.title, "title")
    assert_equal(actual.exercise.course_id, expected.course_id, "course_id")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.order_index, expected.order_index, "order_index")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(actual.exercise.estimated_time, expected.estimated_time, "estimated_time")

@allure.step("Check exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Сравнение данных двух моделей упражнения
    :param actual: Полученный от API ответ
    :param expected: Ожидаемый от API ответ
    :return: AssertionError если хотя бы одно значение не совпадает
    """
    logger.info("Check exercise")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

@allure.step("Check get exercise response")
def assert_get_exercise_response(actual: CreateExerciseResponseSchema, expected: GetExerciseResponseSchema):
    """
    Проверка ответа полученного от API на запрос получения упражнения
    :param actual: Ответ полученный от API при создании упражнения
    :param expected: Ответ полученный от API при запросе упражнения по id
    :return: AssertionError если хотя бы одно значение не совпадает
    """
    logger.info("Check get exercise response")

    assert_exercise(actual.exercise, expected.exercise)

@allure.step("Check update exercise response")
def assert_update_exercise_response(request: UpdateExerciseRequestSchema, response: UpdateExercisesResponseSchema):
    """
    Проверка ответа от API при обновлении упражнения на соответствие ожидаемым данным
    :param request: данные переданные в API при запросе
    :param response: данные полученные от API при ответе
    :return: AssertionError если хотя бы одно значение не совпадает
    """
    logger.info("Check update exercise response")

    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")

@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    проверяет, что ответ на внутреннюю ошибку (404) соответствует ожидаемому
    :param actual: Полученное сообщение об ошибке
    :return: AssertionError если ответ от API не соответствует ожидаемому
    """
    logger.info("Check exercise not found response")

    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_equal(actual, expected, "detail")

@allure.step("Check get exercises response")
def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema, # Возвращает ответ состоящий из списка упражнений
        create_exercise_responses: List[CreateExerciseResponseSchema] # создает и возвращает список из созданных упражнений
):
    """
    Проверяет ответ на запрос списка упражнений на соответствие количеству упражнений и ожидаемой модели ответа
    :param get_exercises_response: Ответ полученный от Апи при запросе списка упражнений
    :param create_exercise_responses: список из упражнений полученный при создании упражнения
    :return: AssertionError если ответ от API не соответствует ожидаемому
    """
    logger.info("Check get exercises response")

    assert_length(get_exercises_response.exercises, create_exercise_responses, "exercises")

    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response.exercise)


