from clients.api_client import ApiClient
from httpx import Response
from clients.courses.courses_schema import GetCoursesSchema, CreateCourseSchema, UpdateCoursesSchema, \
    CreateCourseResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class CoursesApi(ApiClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesSchema) -> Response:
        """
        Метод для получения списка курсов
        :param query: словарь с userId
        :return: Обьект httpx.Response
        """
        return self.get("/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод для получения курса по его Id
        :param course_id: уникальный идентификатор курса
        :return: Обьект httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseSchema) -> Response:
        """
        Метод лоя создания курса
        :param request: title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId
        :return: Обьект httpx.Response
        """
        return self.post("/api/v1/courses", json=request.model_dump(by_alias=True))

    def update_course_api(self, request: UpdateCoursesSchema, course_id: str ) -> Response:
        """
        Методл для обновления курса
        :param request:
        :param course_id: title, maxScore, minScore, description, estimatedTime
        :return: Обьект httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request.model_dump(by_alias=True))

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод для удаления курса
        :param course_id: уникальный идентификатор курса
        :return: Обьект httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")


    def create_course(self, request: CreateCourseSchema) -> CreateCourseResponseSchema:
        """
        Метод для получения ответа на создание курса
        :param request: title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId
        :return: ответа на создание курса в формате json
        """
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

def get_courses_client(user: AuthenticationUserSchema) -> CoursesApi:
    """
    Создаем клиент для работы с курсами
    """
    return CoursesApi(client=get_private_http_client(user))