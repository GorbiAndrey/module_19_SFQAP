import pytest
from app.calculator import Calculator


class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 3, 3) == 1

    def test_division_calculation_failed(self):
        assert self.calc.division(self, 2, 2) == 2

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtracton(self, 2, 2) == 0

    def test_subtraction_calculation_failed(self):
        assert self.calc.subtracton(self, 2, 2) == 2

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 2, 2) == 4

    def test_adding_calculation_failed(self):
        assert self.calc.adding(self, 3, 3) == 9
