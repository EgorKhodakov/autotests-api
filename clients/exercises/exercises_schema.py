from pydantic import BaseModel, Field, ConfigDict


class GetExercisesApiSchema(BaseModel):
    """
    Структура запроса для получения упражнений
    """
    query: str

class CreateExerciseApiSchema(BaseModel):
    """
    Структура запроса для создания упражнения
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score:int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class UpdateExerciseApiSchema(BaseModel):
    """
    Структура запроса для изменения упражнения
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")


class ExerciseSchema(BaseModel):
    """
    Структура упражнения
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class GetExerciseResponseSchema(BaseModel):
    """
    Структура ответа на запрос создания упражнения
    """
    exercise: ExerciseSchema

class GetExercisesResponseSchema(BaseModel):
    """
    Структра ответа на запрос списка упражнений
    """
    exercises: list[ExerciseSchema]

class UpdateExercisesResponseSchema(BaseModel):
    """
    Структура ответа на запрос обновления упражнения
    """
    exercise: ExerciseSchema