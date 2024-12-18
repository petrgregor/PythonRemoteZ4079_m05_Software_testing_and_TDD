"""
Implementujte funkci is_prime(n), která vrátí True, pokud je číslo prvočíslo, jinak vrátí False.
Implementujte funkci factorial(n), která vrátí faktoriál čísla n.
"""
import pytest
from p10_Exercise_prime_factorial import is_prime, factorial


def test_is_prime():
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(17) is True
    assert is_prime(18) is False
    assert is_prime(19) is True


is_prime_parameters = [(-5, False),
                       (0, False),
                       (1, False),
                       (2, True),
                       (3, True),
                       (4, False),
                       (5, True),
                       (6, False),
                       (7, True),
                       (100, False),
                       (101, True)]


@pytest.mark.parametrize("number, result", is_prime_parameters)
def test_is_prime_param(number, result):
    assert is_prime(number) is result


def test_is_prime_exception():
    with pytest.raises(TypeError):
        is_prime("5")
    with pytest.raises(TypeError):
        is_prime(3.7)


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120


factorial_parameters = [(0, 1),
                        (1, 1),
                        (2, 2),
                        (3, 6),
                        (4, 24),
                        (5, 120),
                        (10, 3628800)]


@pytest.mark.parametrize("number, result", factorial_parameters)
def test_factorial_param(number, result):
    assert factorial(number) == result


def test_factorial_exception():
    with pytest.raises(TypeError):
        factorial(3.7)
    with pytest.raises(TypeError):
        factorial("Hi")
    with pytest.raises(ValueError):
        factorial(-8)


if __name__ == "__main__":
    pytest.main()
