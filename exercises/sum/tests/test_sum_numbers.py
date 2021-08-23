import unittest

from exercises.sum import services

class TestSumNumbers(unittest.TestCase):

    SUM_FIRST_HUNDRED_NUMBERS = 5050

    def test_default_arg(self):
        result = services.sum_numbers()
        self.assertEqual(result, self.SUM_FIRST_HUNDRED_NUMBERS )

    def test_fixed_input(self):
        input_ = [1,2,3,4]
        result = services.sum_numbers(input_)
        self.assertEqual(result, 10)
