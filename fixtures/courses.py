import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FilesFixture
from fixtures.users import UserFixture

class CoursesFixture(BaseModel):
    """
    Модель для агрегации возвращаемых данных фикстурой function_course
    """
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema


@pytest.fixture
def course_client(function_user: UserFixture) -> CoursesClient:
    """
    Инициализация клиента CoursesClient
    """
    return get_courses_client(function_user.authentication_user)


@pytest.fixture
def function_course(function_file: FilesFixture,
                    function_user: UserFixture,
                    course_client: CoursesClient) -> CoursesFixture:
    """
    Создание курса
    """

    request = CreateCourseRequestSchema(
        previewFileId=function_file.response.file.id,
        createdByUserId=function_user.response.user.id,
    )
    response = course_client.create_course(request)
    return CoursesFixture(request=request,response=response)


