from pydantic import BaseModel, HttpUrl, Field, FilePath
from tools.fakers import fake


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса для создания файла
    """
    filename: str = Field(default_factory=lambda: f"{fake.uid()}.png")
    directory: str = Field(default="tests")
    upload_file: FilePath

class FileShema(BaseModel):
    """
    Описание структуры файла
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа при создании файла
    """
    file: FileShema


class GetFileResponseSchema(BaseModel):
    file: FileShema