""" Cvičení 4
Funkce get_avg bere ze souboru how_much čísla a počítá jejich průměr. Otestuj funkci get_avg s vědomím,
že očekává pouze čísla v souboru a nemůžeš použít soubor k testování.
"""
from unittest.mock import MagicMock, patch
from p08_Exercise_4 import *


def test_get_avg():
    fake_get_data = MagicMock(return_value="1")
    with patch("p08_Exercise_4._get_data", fake_get_data):
        assert get_avg(1) == 1

    fake_get_data = MagicMock(return_value="12")
    with patch("p08_Exercise_4._get_data", fake_get_data):
        assert get_avg(2) == 1.5

    fake_get_data = MagicMock(return_value="123")
    with patch("p08_Exercise_4._get_data", fake_get_data):
        assert get_avg(3) == 2
