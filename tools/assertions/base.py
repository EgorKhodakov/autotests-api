from typing import Any

def assert_status_code(actual: int, expected: int):
    """
    Функция для проверки корректности статус кода
    :param actual: статус код полученый от апи
    :param expected: ожидаему статус код
    :return: AssertionError: Если статус-коды не совпадают.
    """
    assert actual == expected, (
        'Status cod incorect'
        f'Actual status code {actual} != expected status code {expected}'
    )

def assert_equal(actual: Any, expected: Any, name: str):
    assert actual == expected, (
        f"Field {name} incorrect"
        f'Actual {actual} != expected {expected}'
    )

def assert_is_true(actual: Any, name: str):
    assert actual, (
        f'Field {name} incorrect'
        f'Actual {actual} != expected {True}'
    )