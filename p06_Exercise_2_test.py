import pytest
from p06_Exercise_2 import *

"""Cvičení 2

Máme kód:

def odd_indexes(string):
    return string[1::2]

Pro zadaný řetězec vrací písmena z lichých indexů, př.:

elephant -> lpat computer -> optr

Otestuj tuto funkci se řetězcem jako jejím argumentem.

Spusť funkci s celým číslem. Pozoruj co se stane. Napiš testy pro celočíselné argumenty. Oprav funkci, tak aby fungovala a aby testy prošly.
"""


def test_odd_indexes_str():
    assert odd_indexes("elephant") == "lpat"
    assert odd_indexes("computer") == "optr"
    assert odd_indexes("Petr") == "er"


def test_odd_indexes_int():
    assert odd_indexes(123456789) == "2468"
    assert odd_indexes(3456) == "46"
    assert odd_indexes(159753) == "573"
    assert odd_indexes(0) == ""
    assert odd_indexes(1) == ""
    assert odd_indexes(11) == "1"
    assert odd_indexes(111) == "1"
    assert odd_indexes(1111) == "11"


"""Cvičení 2a

Přepiš předchozí testy, aby využivaly pytest parametrizaci a odstraň duplikaci kódu.
"""


@pytest.mark.parametrize("input_, result", [("elephant", "lpat"), ("computer", "optr"), ("Petr", "er"),
                                           (123456789, "2468"), (0, ""), (1, ""), (11, "1"),
                                           (111, "1"), (1111, "11")])
def test_odd_indexes_param(input_, result):
    assert odd_indexes(input_) == result
