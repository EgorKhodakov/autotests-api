import uuid
from pydantic import BaseModel, Field, EmailStr
from tools.fakers import fake


class UserSchema(BaseModel):
    """
    Модель юзера
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr = Field(default_factory=fake.email)
    last_name: str = Field(alias="lastName", default="Khodakov")
    first_name: str = Field(alias="firstName", default="Egor")
    middle_name: str = Field(alias="middleName", default="Ivanovich")


class CreateUserRequestSchema(BaseModel):
    """
    Модель запроса на создание юзера
    """
    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias="lastName", default="Khodakov")
    first_name: str = Field(alias="firstName", default="Egor")
    middle_name: str = Field(alias="middleName", default="Ivanovich")

class CreateUserResponseSchema(BaseModel):
    """
    Модель ответа на создание пользователя
    """
    user: UserResponseSchema

class UserResponseSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")