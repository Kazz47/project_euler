from problems import Problem010
import unittest

class test_problem010(unittest.TestCase):

    def test_sumOfPrimes_10(self):
        targetIndex = 10
        expectedResult = 17

        actualResult = Problem010.sumOfPrimes(targetIndex)

        self.assertEqual(actualResult, expectedResult)

    def disable_test_sumOfPrimes_2000000(self):
        targetIndex = 2000000
        expectedResult = 142913828922

        actualResult = Problem010.sumOfPrimes(targetIndex)

        self.assertEqual(actualResult, expectedResult)

if __name__ == '__main__':
    unittest.main()

