"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addtition(self):
        assert 4 == calculator.add_num(2, 2)

    def test_multiplication(self):
        assert 1 == calculator.sub_num(3, 2)
