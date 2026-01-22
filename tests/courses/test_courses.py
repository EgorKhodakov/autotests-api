from http import HTTPStatus

import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCoursesRequestSchema, UpdateCourseResponseSchema, \
    GetCoursesQuerySchema, GetCoursesResponseSchema, CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.courses import CoursesFixture
from fixtures.files import FilesFixture
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_get_courses_response, \
    assert_create_course_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_update_course(self, course_client: CoursesClient, function_course: CoursesFixture):

        request = UpdateCoursesRequestSchema()
        response = course_client.update_course_api(request, function_course.response.course.id)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_courses_response(self,
                                  course_client: CoursesClient,
                                  function_course: CoursesFixture,
                                  function_user: UserFixture
                                  ):

        query = GetCoursesQuerySchema(userId=function_user.response.user.id)
        response = course_client.get_courses_api(query)
        response_data= GetCoursesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_get_courses_response(response_data, [function_course.response])

    def test_create_course(
            self,
            course_client: CoursesClient,
            function_user:UserFixture,
            function_file: FilesFixture
    ):

        request = CreateCourseRequestSchema(
            previewFileId=function_file.response.file.id,
            createdByUserId=function_user.response.user.id,

        )
        response = course_client.create_course_api(request)
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_create_course_response(request, response_data)




