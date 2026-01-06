from pydantic import BaseModel, HttpUrl

class CreateFileRequestShema(BaseModel):
    """
    Описание структуры запроса для создания файла
    """
    filename: str
    directory: str
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