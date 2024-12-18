"""Fibonacciho posloupnost
Implementujte funkci fibonacci(n), která vrátí n-tý prvek Fibonacciho posloupnosti.
"""
import pytest
from p12_Exercise_fibonacci import fibonacci, fibonacci_reduce


def test_fibonacci():
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(3) == 1
    assert fibonacci(4) == 2
    assert fibonacci(5) == 3
    assert fibonacci(6) == 5
    assert fibonacci(100) == 218922995834555169026


params = [(1, 0), (2, 1), (3, 1), (4, 2), (5, 3), (6, 5), (100, 218922995834555169026)]


@pytest.mark.parametrize("number, result", params)
def test_fibonacci_param(number, result):
    assert fibonacci(number) == result


@pytest.mark.parametrize("number, result", params)
def test_fibonacci_reduce_param(number, result):
    assert fibonacci_reduce(number) == result


def test_fibonacci_exception():
    with pytest.raises(TypeError):
        fibonacci("5")
    with pytest.raises(TypeError):
        fibonacci(1.7)
    with pytest.raises(ValueError):
        fibonacci(0)
    with pytest.raises(ValueError):
        fibonacci(-5)


if __name__ == "__main__":
    pytest.main()
