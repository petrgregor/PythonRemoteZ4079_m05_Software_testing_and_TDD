import pytest

from p02_ComplexNumber import *


class Test:

    def setup_method(self):
        print("setup")

    def teardown_method(self):
        print("\tend")

    def test_init(self):
        complex_number = ComplexNumber(2, 3)
        assert complex_number.re == 2
        assert complex_number.img == 3
        with pytest.raises(Exception):
            complex_number = ComplexNumber("Hi", 5)
        with pytest.raises(Exception):
            complex_number = ComplexNumber(5, "hi")
        with pytest.raises(Exception):
            complex_number = ComplexNumber("Hello", "world")
        with pytest.raises(Exception):
            complex_number = ComplexNumber(None, None)

    def test_eq(self):
        assert ComplexNumber(1, 3) == ComplexNumber(1, 3)
        assert ComplexNumber(2, 5) != ComplexNumber(5, 2)

    def test_lt(self):
        assert ComplexNumber(1, 2) < ComplexNumber(5, 8)

    def test_gt(self):
        assert ComplexNumber(10, 20) > ComplexNumber(5, 8)

    def test_repr(self):
        assert ComplexNumber(2, 3).__repr__() == "ComplexNumber(re=2, img=3)"
        assert ComplexNumber(5, -4).__repr__() == "ComplexNumber(re=5, img=-4)"

    def test_str(self):
        assert ComplexNumber(2, 3).__str__() == "2 + 3i"
        assert ComplexNumber(5, -4).__str__() == "5 - 4i"

    def test_getter(self):
        complex_number = ComplexNumber(2, 6)
        assert complex_number.re == 2

    def test_setter(self):
        complex_number = ComplexNumber(2, 6)
        assert complex_number.img == 6

    @pytest.mark.skip("Not implemented")
    def test_add(self):
        pass

    @pytest.mark.skip("Not implemented")
    def test_subtract(self):
        pass

    @pytest.mark.skip("Not implemented")
    def test_multiply(self):
        pass

    @pytest.mark.skip("Not implemented")
    def test_divide(self):
        pass

    @pytest.mark.skip("Not implemented")
    def test_conjugate(self):
        pass

    @pytest.mark.skip("Not implemented")
    def test_abs(self):
        pass
