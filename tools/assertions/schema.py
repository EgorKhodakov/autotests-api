from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator


def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверяет, соответствует ли обьект JSON заданой JSON схеме
    :param instance: ответ от АПИ (схема которую нужно проверить)
    :param schema: ожидаемые данные
    :raises jsonschema.exceptions.ValidationError: Если instance не соответствует schema.
    """
    validate(instance=instance,
             schema=schema,
             format_checker=Draft202012Validator.FORMAT_CHECKER
             )