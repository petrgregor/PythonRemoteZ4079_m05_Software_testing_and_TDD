"""Počítání slov
Implementujte funkci word_count(s), která vrátí počet slov v daném řetězci.
"""
import pytest
from p11_Exercise_word_count import word_count


def test_word_count():
    assert word_count("Hello     world") == 2
    assert word_count("This is a test") == 4
    assert word_count("One more test case") == 4
    assert word_count("") == 0
    assert word_count("Python is awesome!") == 3


params = [("Hello     world", 2),
          ("This is a test", 4),
          ("One more test case", 4),
          ("", 0),
          ("Python is awesome!", 3),
          ("    ", 0),
          (123, 1)]


@pytest.mark.parametrize("s, result", params)
def test_word_count_param(s, result):
    assert word_count(s) == result


if __name__ == "__main__":
    pytest.main()
