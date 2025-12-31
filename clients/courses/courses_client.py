from idlelib.squeezer import count_lines_with_wrapping

from clients.api_client import ApiClient
from typing import TypedDict
from httpx import Response

from clients.files.files_client import File
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client
from clients.users.private_users_client import User


class GetCoursesDict(TypedDict):
    """
    Структура запроса для полученичя списка курсов
    """
    userId: str

class CreateCourseDict(TypedDict):
    """
    Структура запроса для создания курса
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateCoursesDict(TypedDict):
    """
    Структура запроса для обновления курса
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class Course(TypedDict):
    """
    Структура курса
    """
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: User

class CreateCourseResponse(TypedDict):
    """
    Структура ответа на создание куоса
    """
    course: Course


class CoursesApi(ApiClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesDict) -> Response:
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

    def create_course_api(self, request: CreateCourseDict) -> Response:
        """
        Метод лоя создания курса
        :param request: title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId
        :return: Обьект httpx.Response
        """
        return self.post("/api/v1/courses", json=request)

    def update_course_api(self, request: UpdateCoursesDict, course_id: str ) -> Response:
        """
        Методл для обновления курса
        :param request:
        :param course_id: title, maxScore, minScore, description, estimatedTime
        :return: Обьект httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод для удаления курса
        :param course_id: уникальный идентификатор курса
        :return: Обьект httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")


    def create_course(self, request: CreateCourseDict) -> CreateCourseResponse:
        """
        Метод для получения ответа на создание курса
        :param request: title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId
        :return: ответа на создание курса в формате json
        """
        return self.create_course_api(request).json()

def get_courses_client(user: AuthenticationUserDict) -> CoursesApi:
    """
    Создаем клиент для работы с курсами
    """
    return CoursesApi(client=get_private_http_client(user))