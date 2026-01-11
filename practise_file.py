# def numbers(numbers: list) -> dict:
#     summ = sum(numbers)
import pytest

@pytest.mark.slowr
def test_heavy_calculation():
    pass

@pytest.mark.integrationr
def test_integration_with_external_api():
    pass

@pytest.mark.smoker
def test_quick_check():
    pass