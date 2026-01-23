from http import HTTPStatus

import pytest

from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema
from fixtures.courses import CoursesFixture
from fixtures.exercises import ExersiceFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise, assert_get_exercise
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.exercises
class TestExercises:
    
    def test_create_exercise(self,function_course: CoursesFixture, exercises_client: ExercisesClient) -> None:
        request = CreateExerciseRequestSchema(
            courseId=function_course.response.course.id
        )
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_create_exercise(response_data, request)


    def test_get_exercise(self, exercises_client: ExercisesClient, function_exercise: ExersiceFixture) -> None:

        response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_get_exercise(function_exercise.response, response_data)


