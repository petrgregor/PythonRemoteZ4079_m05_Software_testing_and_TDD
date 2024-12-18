import pytest
from p09_Exercise_5 import *


def test_product_init():
    product = Product("Item1", 10)
    assert product.volume == 10
    product = Product("Item2", 3.14)
    assert product.volume == 3.14
    with pytest.raises(ValueError):
        Product("Item1", -5)
    with pytest.raises(ValueError):
        Product("Item1", 0)


def test_magazine_init():
    magazine = Magazine(50)
    assert magazine.capacity == 50
    magazine = Magazine(5.15)
    assert magazine.capacity == 5.15
    with pytest.raises(ValueError):
        Magazine(-50)
    with pytest.raises(ValueError):
        Magazine(0)


def test_magazine_add():
    magazine = Magazine(50)
    product = Product("Item3", 20)
    assert magazine.add(product) == 30
    assert magazine.add(product) == 10
    assert magazine.add(product) == -1

    magazine = Magazine(123.45)
    product = Product("Item4", 12.34)
    assert magazine.add(product) == 111.11
    assert magazine.add(product) == 98.77
    assert magazine.add(product) == 86.43
    assert magazine.add(product) == 74.09
    assert magazine.add(product) == 61.75
    assert magazine.add(product) == 49.41
    product2 = Product("Item5", 49.49)
    assert magazine.add(product2) == -1

    magazine = Magazine(9.99)
    product = Product("Item6", 3.33)
    assert magazine.add(product) == 6.66
    assert magazine.add(product) == 3.33
    assert magazine.add(product) == 0


@pytest.fixture
def products():
    return [Product("Item7", 11.11),
            Product("Item8", 22.22),
            Product("Item9", 15),
            Product("Item10", 10)]


@pytest.mark.parametrize("capacity, result", [(50, -1), (58.33, 0), (60, 1.67)])
def test_magazine_add_parametrized(capacity, result, products):
    magazine = Magazine(capacity)
    my_result = None
    for product in products:
        my_result = magazine.add(product)
    assert round(my_result, 2) == result


# TODO test_product_repr
# TODO test_product_str
# TODO test_magazine_repr
# TODO test_magazine_str
