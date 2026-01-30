from typing import Any, Sized
import allure
from tools.logger import get_logger

logger = get_logger("BASE_ASSERTIONS")

@allure.step("Check that response status code equals to {expected}")
def assert_status_code(actual: int, expected: int):
    """
    Функция для проверки корректности статус кода
    :param actual: статус код полученый от апи
    :param expected: ожидаему статус код
    :return: AssertionError: Если статус-коды не совпадают.
    """
    logger.info(f"Check that response status code equals to {expected}")

    assert actual == expected, (
        'Status cod incorect'
        f'Actual status code {actual} != expected status code {expected}'
    )

@allure.step("Check that name equals to {expected}")
def assert_equal(actual: Any, expected: Any, name: str):
    """
    Выполняет сравнение двух значений
    :param actual: полученное от API значение
    :param expected: ожидаемое от API значение
    :param name: название проверяемого параметра
    :return: AssertionError если проверяемые значения не равны
    """
    logger.info(f'Check that "{name}" equals to {expected}')

    assert actual == expected, (
        f"Field {name} incorrect " 
        f'Actual:{actual}'
        f'Expected:{expected}'
    )

@allure.step("Check that {name} is true")
def assert_is_true(actual: Any, name: str):
    """
        Проверяет, что фактическое значение является истинным.

        :param name: Название проверяемого значения.
        :param actual: Фактическое значение.
        :raises AssertionError: Если фактическое значение ложно.
        """
    logger.info(f'Check that "{name}" is true')

    assert actual, (
        f'Field {name} incorrect'
        f'Actual {actual} != expected {True}'
    )


def assert_length(actual: Sized, expected: Sized, name: str) -> None:
    """
    Функция позволяющая сравнивать длину двух обьектов
    :param actual: значение фактически полученное от API
    :param expected: значение ожидаемое отт API
    :param name: название проверяемого параметра
    :return: AssertionError если одно из значений не совпадает
    """


    with allure.step(f"Check that lenght of {name} actual to {len(expected)} "):
        logger.info(f'Check that lenght of "{name}" actual to {len(expected)}')
        assert len(actual) == len(expected), (
            f"incorrect length {name}"
            f"Actual: {len(actual)} Expected: {len(expected)}"
        )