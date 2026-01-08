from pydantic import BaseModel, HttpUrl, Field
from tools.fakers import fake


class CreateFileRequestShema(BaseModel):
    """
    Описание структуры запроса для создания файла
    """
    filename: str = Field(default_factory=lambda: f"{fake.uid()}.png")
    directory: str = Field(default="tests")
    upload_file: str

class FileShema(BaseModel):
    """
    Описание структуры файла
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileResponseShema(BaseModel):
    """
    Описание структуры ответа при создании файла
    """
    file: FileShema