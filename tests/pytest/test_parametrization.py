import pytest
from _pytest.fixtures import  SubRequest


@pytest.mark.parametrize("num1", [pytest.param(-2, marks=pytest.mark.xfail), 1, 2, 3, 4])
def test_numbers(num1:int):
    assert num1 > 0


@pytest.mark.parametrize("expected_count", [1, 2, 0, -15, 30] )
@pytest.mark.parametrize("num1, num2", [(1,1), (2,4), (3,9), (-4,6), ])
def test_count_numbers(num1: int, num2: int, expected_count: int):
    assert  num1  + num2 > expected_count


@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
def host(request:SubRequest) -> str:
    return request.param


def test_host(host: str):
    print (f"тест запущен на хосте {host}")
