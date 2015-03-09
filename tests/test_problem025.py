from problems import Problem025
import unittest

class test_problem025(unittest.TestCase):

    def test_lenFib_3_12(self):
        x = 3
        expectedValue = 12

        actualValue = Problem025.lenFib(x)
        self.assertEqual(expectedValue, actualValue)

    def test_lenFib_1000_4782(self):
        x = 1000
        expectedValue = 4782

        actualValue = Problem025.lenFib(x)
        self.assertEqual(expectedValue, actualValue)

if __name__ == '__main__':
    unittest.main()

