from httpx import Response
from typing import TypedDict
from clients.api_client import ApiClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class GetExercisesApiDict(TypedDict):
    """
    Структура запроса для получения упражнений
    """
    query: str

class CreateExerciseApiDict(TypedDict):
    """
    Структура запроса для создания упражнения
    """
    title: str
    courseId: str
    maxScore: int
    minScore:int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseApiDict(TypedDict):
    """
    Структура запроса для изменения упражнения
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class Exercise(TypedDict):
    """
    Структура упражнения
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExerciseResponseDic(TypedDict):
    """
    Структура ответа на запрос создания, обновления или получения упражнения
    """
    exercise: Exercise

class GetExercisesResponseDict(TypedDict):
    """
    Структра ответа на запрос списка упражнений
    """
    exercises: list[Exercise]

class ExercisesClient(ApiClient):
    """
    Класс для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query:GetExercisesApiDict) -> Response:
        """
        Метод для получения списка упражнений
        :param query: словарь с courseId
        :return: обьект типа httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id:str) -> Response:
        """
        Метод для получения конкретного упражнения
        :param exercise_id: уникальный идентификатор упражнения
        :return: обьект типа httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request:CreateExerciseApiDict ) -> Response:
        """
        Метод для создания упражнения
        :param request: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: обьект типа httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id:str, request:UpdateExerciseApiDict ) -> Response:
        """
        Метод для обновления упраженения
        :param exercise_id:уникальный идентификатор упражнения
        :param request: title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: обьект типа httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id:str) -> Response:
        """
        Метод для удаления упражнения
        :param exercise_id:exercise_id:уникальный идентификатор упражнения
        :return: обьект типа httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id:str) -> GetExerciseResponseDic:
        """
        метод для возврата ответа на запрос о получении упражениы
        :param exercise_id: уникальный идентификатор упражнения
        :return: ответ в формате json
        """
        return self.get_exercise_api(exercise_id).json()

    def get_exercises(self, query:GetExercisesApiDict) -> GetExercisesResponseDict:
        """
        Метод ля получения списка упражнений
        :param query: словарь с courseId
        :return: ответ в формате json
        """
        return self.get_exercise_api(query).json()

    def create_exercise(self, request:CreateExerciseApiDict ) -> GetExerciseResponseDic:
        """
        Метод для создания упражнения
        :param request: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ в формате json
        """
        return self.create_exercise_api(request).json()

    def update_exercise(self, exercise_id:str, request:UpdateExerciseApiDict ) -> GetExerciseResponseDic:
        """
        Метод для обновления упражнения
        :param exercise_id: уникальный идентификатор упражнения
        :param request:  title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ в формате json
        """
        return self.update_exercise_api(exercise_id, request).json()

def get_exercise_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Готовый клиент для работы с упражнениями
    :param user: email, password
    :return: готтовый экземпляр класса ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user))