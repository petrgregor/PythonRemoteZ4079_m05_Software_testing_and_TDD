import pytest

from p01_BasicCalculator import *

parameters = [(-6, -4, -10), (-3, 4, 1), (0, 0, 0), (1, -1, 0), ("5", 5, None)]


@pytest.mark.parametrize("num1, num2, result", parameters)
def test_addition(num1, num2, result):
    calc = BasicCalculator()
    assert calc.add(num1, num2) == result
