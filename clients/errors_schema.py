from typing import Any, Annotated

from pydantic import BaseModel, Field, ConfigDict

class ValidationErrorSchema(BaseModel):
    """
    Модель описывающая структуру ошибки валидации API
    """
    model_config = ConfigDict(populate_by_name=True)

    type: str
    location: Annotated[list[str], Field(alias='loc')]
    message: Annotated[str, Field(alias='msg')]
    input: Any
    context: Annotated[dict[str, Any], Field(alias='ctx')]


class ValidationErrorResponseSchema(BaseModel):
    """
    Модель описывающая структуру ответа API при ошибке валидации
    """
    model_config = ConfigDict(populate_by_name=True)

    details: Annotated[list[ValidationErrorSchema], Field(alias='detail')]


class InternalErrorResponseSchema(BaseModel):
    """
    Модель описывающая структуру внутренней ошибки (404)
    """
    model_config = ConfigDict(populate_by_name=True)

    details: Annotated[str, Field(alias='detail')]


