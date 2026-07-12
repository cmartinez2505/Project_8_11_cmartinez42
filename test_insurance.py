"""
Program Name: Insurance Quote Generator App
Name: Chris Martinez
File Purpose: Tests if our code works as it is supposed to.
Resources used: Python Crash Course (Chapters 8-11)
Date: July 12, 2026
"""

import unittest
from insurance_system import QuoteCalculator

class TestInsuranceCalculator(unittest.TestCase):
    "Tests our calculations to see if they calculate correctly"

    def test_basic_quote(self):
        """Test a basic normal driver with no accidents to make sure the math works"""
        calculator = QuoteCalculator()

        rate = calculator.calculate_quote(30, 2022, 65000, 10, 0)
        self.assertTrue(rate > 0)
    