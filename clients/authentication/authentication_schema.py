from pydantic import BaseModel, Field

class LoginRequestSchema(BaseModel):
    """
    Структура запроса для аутентификации пользователя
    """
    email: str
    password: str


class RefreshRequestSchema(BaseModel):
    """
    Структура запроса для обновления токена
    """
    refresh_token: str = Field(alias="refreshToken")


class LoginResponseSchema(BaseModel):
    """
    Описаине структуры ответа ацтентификации
    """
    token: TokenSchema


class TokenSchema(BaseModel):
    """
    Структура токена аутентификации
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")