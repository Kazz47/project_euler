from problems import Problem7
import unittest

class test_problem7(unittest.TestCase):

    def test_findPrime_6_13(self):
        primeIndex = 6
        expectedResult = 13

        actualResult = Problem7.findPrime(primeIndex)

        self.assertEqual(actualResult, expectedResult)

    def test_findPrime_2_1(self):
        primeIndex = 1
        expectedResult = 2

        actualResult = Problem7.findPrime(primeIndex)

        self.assertEqual(actualResult, expectedResult)

    def test_findPrime_10001_104743(self):
        primeIndex = 10001
        expectedResult = 104743

        actualResult = Problem7.findPrime(primeIndex)

        self.assertEqual(actualResult, expectedResult)


if __name__ == '__main__':
    unittest.main()
