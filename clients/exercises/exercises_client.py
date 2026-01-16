from httpx import Response
from clients.api_client import ApiClient
from clients.exercises.exercises_schema import GetExercisesSchema, CreateExerciseSchema, UpdateExerciseSchema, \
    GetExerciseResponseSchema, GetExercisesResponseSchema, UpdateExercisesResponseSchema, CreateExerciseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class ExercisesClient(ApiClient):
    """
    Класс для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query:GetExercisesSchema) -> Response:
        """
        Метод для получения списка упражнений
        :param query: словарь с courseId
        :return: обьект типа httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id:str) -> Response:
        """
        Метод для получения конкретного упражнения
        :param exercise_id: уникальный идентификатор упражнения
        :return: обьект типа httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request:CreateExerciseSchema ) -> Response:
        """
        Метод для создания упражнения
        :param request: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: обьект типа httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id:str, request:UpdateExerciseSchema ) -> Response:
        """
        Метод для обновления упраженения
        :param exercise_id:уникальный идентификатор упражнения
        :param request: title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: обьект типа httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id:str) -> Response:
        """
        Метод для удаления упражнения
        :param exercise_id:exercise_id:уникальный идентификатор упражнения
        :return: обьект типа httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id:str) -> GetExerciseResponseSchema:
        """
        метод для возврата ответа на запрос о получении упражениы
        :param exercise_id: уникальный идентификатор упражнения
        :return: ответ в формате json
        """
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query:GetExercisesSchema) -> GetExercisesResponseSchema:
        """
        Метод ля получения списка упражнений
        :param query: словарь с courseId
        :return: ответ в формате json
        """
        response = self.get_exercise_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request:CreateExerciseSchema ) -> CreateExerciseResponseSchema:
        """
        Метод для создания упражнения
        :param request: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ в формате json
        """
        return self.create_exercise_api(request).json()

    def update_exercise(self, exercise_id:str, request:UpdateExerciseSchema ) -> UpdateExercisesResponseSchema:
        """
        Метод для обновления упражнения
        :param exercise_id: уникальный идентификатор упражнения
        :param request:  title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ в формате json
        """
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExercisesResponseSchema.model_validate_json(response.text)

def get_exercise_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Готовый клиент для работы с упражнениями
    :param user: email, password
    :return: готтовый экземпляр класса ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user))