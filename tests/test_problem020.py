from problems import Problem020
import unittest

class test_problem020(unittest.TestCase):

    def test_sumFactoral_10_27(self):
        x = 10
        expectedValue = 27

        actualValue = Problem020.sumFactorial(x)
        self.assertEqual(expectedValue, actualValue)

    def test_sumPower_100_(self):
        x = 100
        expectedValue = 648

        actualValue = Problem020.sumFactorial(x)
        self.assertEqual(expectedValue, actualValue)

if __name__ == '__main__':
    unittest.main()

