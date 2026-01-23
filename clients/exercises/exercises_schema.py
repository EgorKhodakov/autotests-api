from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake


class GetExercisesSchema(BaseModel):
    """
    Структура запроса для получения упражнений
    """
    query: str

class CreateExerciseRequestSchema(BaseModel):
    """
    Структура запроса для создания упражнения
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uid)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score:int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class UpdateExerciseRequestSchema(BaseModel):
    """
    Структура запроса для изменения упражнения
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int | None = Field(alias="orderIndex", default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)


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

class CreateExerciseResponseSchema(BaseModel):
    """
    Структура ответа на создание упражнения
    """
    exercise: ExerciseSchema