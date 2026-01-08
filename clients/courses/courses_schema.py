from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileShema
from clients.users.users_schema import UserSchema
from tools.fakers import fake


class GetCoursesSchema(BaseModel):
    """
    Структура запроса для полученичя списка курсов
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")
    course_id: str = Field(alias="courseId")

class CreateCourseSchema(BaseModel):
    """
    Структура запроса для создания курса
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentance)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uid)
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uid)

class UpdateCoursesSchema(BaseModel):
    """
    Структура запроса для обновления курса
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=fake.sentance)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class CourseSchema(BaseModel):
    """
    Структура курса
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileShema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")

class CreateCourseResponseSchema(BaseModel):
    """
    Структура ответа на создание куоса
    """
    course: CourseSchema