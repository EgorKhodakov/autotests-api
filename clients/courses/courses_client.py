import allure

from clients.api_client import ApiClient
from httpx import Response
from clients.courses.courses_schema import (GetCoursesQuerySchema, CreateCourseRequestSchema,
                                            CreateCourseResponseSchema, UpdateCoursesRequestSchema)
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from tools.routes import APIRoutes


class CoursesClient(ApiClient):
    """
    Клиент для работы с /api/v1/courses
    """

    @allure.step("Get Courses")
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод для получения списка курсов
        :param query: словарь с userId
        :return: Объект httpx.Response
        """
        return self.get(APIRoutes.COURSES, params=query.model_dump(by_alias=True))

    @allure.step("Get course by id {course_id}")
    def get_course_api(self, course_id: str) -> Response:
        """
        Метод для получения курса по его Id
        :param course_id: уникальный идентификатор курса
        :return: Объект httpx.Response
        """
        return self.get(f"{APIRoutes.COURSES}/{course_id}")

    @allure.step("Create Course")
    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод лоя создания курса
        :param request: title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId
        :return: Объект httpx.Response
        """
        return self.post("/api/v1/courses", json=request.model_dump(by_alias=True))

    @allure.step("Update Courses by id {course_id}")
    def update_course_api(self, request: UpdateCoursesRequestSchema, course_id: str ) -> Response:
        """
        Методл для обновления курса
        :param request:
        :param course_id: title, maxScore, minScore, description, estimatedTime
        :return: Объект httpx.Response
        """
        return self.patch(f"{APIRoutes.COURSES}/{course_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete Courses by id {course_id}")
    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод для удаления курса
        :param course_id: уникальный идентификатор курса
        :return: Объект httpx.Response
        """
        return self.delete(f"{APIRoutes.COURSES}/{course_id}")


    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Метод для получения ответа на создание курса
        :param request: title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId
        :return: ответ на создание курса в формате json
        """
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Создаем клиент для работы с курсами
    """
    return CoursesClient(client=get_private_http_client(user))