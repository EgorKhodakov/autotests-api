from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileShema
from clients.users.users_schema import UserSchema


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

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")

class UpdateCoursesSchema(BaseModel):
    """
    Структура запроса для обновления курса
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")

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