from problems import Problem007
import unittest

class test_problem007(unittest.TestCase):

    def test_findPrime_6_13(self):
        primeIndex = 6
        expectedResult = 13

        actualResult = Problem007.findPrime(primeIndex)

        self.assertEqual(actualResult, expectedResult)

    def test_findPrime_2_1(self):
        primeIndex = 1
        expectedResult = 2

        actualResult = Problem007.findPrime(primeIndex)

        self.assertEqual(actualResult, expectedResult)

    def test_findPrime_10001_104743(self):
        primeIndex = 10001
        expectedResult = 104743

        actualResult = Problem007.findPrime(primeIndex)

        self.assertEqual(actualResult, expectedResult)


if __name__ == '__main__':
    unittest.main()

