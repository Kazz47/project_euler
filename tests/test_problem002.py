from problems import Problem002
import unittest

class test_problem002(unittest.TestCase):

    def test_fibonacci_10_10(self):
        maxVal = 10
        expectedValue = 10

        actualValue = Problem002.fibonacciSum(2, maxVal)

        self.assertEqual(actualValue % 2, 0)
        self.assertEqual(actualValue, expectedValue)

    def test_fibonacci_4000000_10(self):
        maxVal = 4000000
        expectedValue = 4613732

        actualValue = Problem002.fibonacciSum(2, maxVal)

        self.assertEqual(actualValue % 2, 0)
        self.assertEqual(expectedValue, actualValue)

if __name__ == '__main__':
    unittest.main()

