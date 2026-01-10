from pydantic import BaseModel, Field
from tools.fakers import fake


class LoginRequestSchema(BaseModel):
    """
    Структура запроса для аутентификации пользователя
    """
    email: str = Field(default=fake.email())
    password: str = Field(default_factory=fake.password)


class RefreshRequestSchema(BaseModel):
    """
    Структура запроса для обновления токена
    """
    refresh_token: str = Field(alias="refreshToken", default=fake.sentence)


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