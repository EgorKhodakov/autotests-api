from http import HTTPStatus

import allure
import pytest

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExercisesResponseSchema, GetExercisesSchema, \
    GetExercisesResponseSchema
from fixtures.courses import CoursesFixture
from fixtures.exercises import ExersiceFixture
from tools.allure.tags import AllureTag
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.epics import AllureEpic
from allure_commons.types import Severity
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_update_exercise_response, \
    assert_exercise_not_found_response, assert_get_exercise_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.exercises
@allure.tag(AllureTag.CREATE_ENTITY, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.EXERCISES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.EXERCISES)
class TestExercises:

    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("test create exercise")
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_exercise(self,function_course: CoursesFixture, exercises_client: ExercisesClient) -> None:
        request = CreateExerciseRequestSchema(
            courseId=function_course.response.course.id
        )
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_create_exercise_response(response_data, request)

    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("test get exercise")
    @allure.story(AllureStory.GET_ENTITY)
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    def test_get_exercise(self, exercises_client: ExercisesClient, function_exercise: ExersiceFixture) -> None:

        response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_get_exercise_response(function_exercise.response, response_data)

    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.title("test update exercise")
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    def test_update_exercise(self, exercises_client: ExercisesClient, function_exercise: ExersiceFixture) -> None:

        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(
            function_exercise.response.exercise.id,
            request
        )
        response_data = UpdateExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_update_exercise_response(request, response_data)

    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.title("test delete exercise")
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.DELETE_ENTITY)
    def test_delete_exercise(self, exercises_client: ExercisesClient, function_exercise: ExersiceFixture) -> None:

        exercise_id = function_exercise.response.exercise.id
        delete_response = exercises_client.delete_exercise_api(exercise_id)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        response = exercises_client.get_exercise_api(exercise_id)
        response_data = InternalErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("test get exercises")
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.GET_ENTITIES)
    def test_get_exercises(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExersiceFixture,
            function_course: CoursesFixture
    ) -> None:

        query = GetExercisesSchema(
            courseId=function_course.response.course.id
        )

        response = exercises_client.get_exercises_api(query)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_get_exercises_response(response_data, [function_exercise.response])




