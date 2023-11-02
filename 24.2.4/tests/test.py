import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply(self):
        assert self.calc.multiply(self, 2, 5) == 10

    def test_division(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_division_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_subtraction(self):
        assert self.calc.subtraction(self, 1, 1) == 0

    def test_adding(self):
        assert self.calc.adding(self, 1, 1) == 2

    def teardown(self):
        print('Выполнение метода Teardown')