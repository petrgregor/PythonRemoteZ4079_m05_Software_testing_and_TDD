import pytest

from p01_BasicCalculator import BasicCalculator


class Test:
    def setup_method(self):
        print("setup_method: Tato metoda se spustí jednou na začátku každého testu "
              "a slouží k nastavení prostředí pro test.")

    def test_addition(self):
        basic_calculator = BasicCalculator()
        result = basic_calculator.add(3, 5)
        assert result == 8
        assert basic_calculator.add(-6, -4) == -10
        assert basic_calculator.add(-3, 4) == 1
        assert basic_calculator.add(3, -4) == -1
        assert basic_calculator.add(3, 0) == 3
        assert basic_calculator.add("3", "5") is None
        assert basic_calculator.add("Hello", "World") is None
        assert basic_calculator.add(3, "5") is None
        assert round(basic_calculator.add(2.1, 3.2), 1) == 5.3
        assert basic_calculator.add([5], 2) is None

    def test_subtraction(self):
        basic_calculator = BasicCalculator()
        result = basic_calculator.subtract(3, 5)
        assert result == -2
        assert basic_calculator.subtract(-6, -4) == -2
        assert basic_calculator.subtract(-3, 4) == -7
        assert basic_calculator.subtract(3, -4) == 7
        assert basic_calculator.subtract(3, 0) == 3
        assert basic_calculator.subtract(0, 3) == -3
        assert basic_calculator.subtract("3", "5") is None
        assert basic_calculator.subtract("Hello", "World") is None
        assert basic_calculator.subtract(3, "5") is None
        assert round(basic_calculator.subtract(2.1, 3.2), 1) == -1.1
        assert basic_calculator.subtract([5], 2) is None

    def test_multiply(self):
        basic_calculator = BasicCalculator()
        result = basic_calculator.multiply(3, 5)
        assert result == 15
        assert basic_calculator.multiply(-6, -4) == 24
        assert basic_calculator.multiply(-3, 4) == -12
        assert basic_calculator.multiply(3, -4) == -12
        assert basic_calculator.multiply(3, 0) == 0
        assert basic_calculator.multiply(0, 3) == 0
        assert basic_calculator.multiply("3", "5") is None
        assert basic_calculator.multiply("Hello", "World") is None
        assert basic_calculator.multiply(3, "5") is None
        assert round(basic_calculator.multiply(2.1, 3.2), 2) == 6.72
        assert basic_calculator.multiply([5], 2) is None

    @pytest.mark.skip("Dělení chci přeskočit")
    def test_divide(self):
        basic_calculator = BasicCalculator()
        result = basic_calculator.divide(8, 2)
        assert result == 4
        assert basic_calculator.divide(-12, -4) == 3
        assert basic_calculator.divide(-12, 4) == -3
        assert basic_calculator.divide(12, -4) == -3
        assert basic_calculator.divide(3, 0) is None
        assert basic_calculator.divide(0, 3) == 0
        assert basic_calculator.divide("3", "5") is None
        assert basic_calculator.divide("Hello", "World") is None
        assert basic_calculator.divide(3, "5") is None
        assert round(basic_calculator.divide(2.1, 3.2), 5) == 0.65625
        assert basic_calculator.divide([5], 2) is None

        # testování vyjímky
        with pytest.raises(Exception):
            assert basic_calculator.divide2(8, 0)

    def teardown_method(self):
        print("\tteardown_method: Spustí se na konci každého testu "
              "a slouží k vyčištění testovacího prostředí.")
