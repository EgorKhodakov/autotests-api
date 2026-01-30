from typing import List

import allure

from clients.courses.courses_schema import UpdateCourseResponseSchema, UpdateCoursesRequestSchema, \
    GetCoursesResponseSchema, CourseSchema, CreateCourseResponseSchema, CreateCourseRequestSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user
from tools.logger import get_logger

logger = get_logger("COURSE_ASSERTIONS")

@allure.step("Check update course response")
def assert_update_course_response(
        request: UpdateCoursesRequestSchema,
        response: UpdateCourseResponseSchema):
    """
    Проверяет ответ от API на обновление курса соответствует данным из запроса
    :param request: Исходный запрос на обновление курса
    :param response: Ответ от API с обновленными данными
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check update course response")

    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")

@allure.step("Check course")
def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Проверяет, что фактические данные курса соответствуют ожидаемым.
    :param actual:  Фактические данные курса.
    :param expected: Ожидаемые данные курса.
    :return:AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check course")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)

@allure.step("Check get courses response")
def assert_get_courses_response(
        get_courses_response: GetCoursesResponseSchema,
        create_course_responses: List[CreateCourseResponseSchema]):
    """
    Проверяет, что ответ на получение списка курсов соответствует ответам на их создание.
    :param get_courses_response: Данные переданные в API
    :param create_course_responses: Данные полученные от API
    :return:AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check get courses response")

    assert_length(get_courses_response.courses, create_course_responses, "courses")

    for index, create_course_response in enumerate(create_course_responses):
        assert_course(get_courses_response.courses[index], create_course_response.course)

@allure.step("Check create course response")
def assert_create_course_response(request: CreateCourseRequestSchema, response: CreateCourseResponseSchema):
    """
    Проверка соответствия данных при создании курса
    :param request: Запрос переданный API
    :param response: Ответ полученный от API
    :return:AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check create course response")

    assert_equal(request.title, response.course.title, "id")
    assert_equal(request.max_score, response.course.max_score, "max_score")
    assert_equal(request.min_score, response.course.min_score, "min_score")
    assert_equal(request.description, response.course.description, "description")
    assert_equal(request.estimated_time, response.course.estimated_time, "estimated_time")
    assert_equal(request.preview_file_id, response.course.preview_file.id, "id")
    assert_equal(request.created_by_user_id, response.course.created_by_user.id, "id")



