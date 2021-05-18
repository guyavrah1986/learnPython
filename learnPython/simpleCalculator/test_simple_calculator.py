import unittest

from learnPython.simpleCalculator.simpleCalculator import SimpleCalculator

class SimpleCalculatorTestCase(unittest.TestCase):

    def test_add_function(self):
        func_name = "SimpleCalculatorTestCase::test_something - "
        print(func_name + "start")
        tested_obj = SimpleCalculator()
        num1 = 7
        num2 = 8
        res = num1 + num2
        self.assertEqual(tested_obj.add(num1, num2), res)


if __name__ == '__main__':
    unittest.main()