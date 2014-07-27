import unittest
import Problem3

class Problem3Tests(unittest.TestCase):

    def test_isPrime_1_true(self):
        val = 1
        expectedResult = True

        actualResult = Problem3.isPrime(val)

        self.assertEqual(actualResult, expectedResult)

    def test_isPrime_2_true(self):
        val = 2
        expectedResult = True

        actualResult = Problem3.isPrime(val)

        self.assertEqual(actualResult, expectedResult)

    def test_isPrime_3_true(self):
        val = 3
        expectedResult = True

        actualResult = Problem3.isPrime(val)
        
        self.assertEqual(actualResult, expectedResult)

    def test_isPrime_4_false(self):
        val = 4
        expectedResult = False

        actualResult = Problem3.isPrime(val)

        self.assertEqual(actualResult, expectedResult)
    
    def test_isPrime_29_true(self):
        val = 29
        expectedResult = True

        actualResult = Problem3.isPrime(val)

        self.assertEqual(actualResult, expectedResult)

    def test_factor_1_empty(self):
        val = 1
        expectedResult = []


        actualResult = Problem3.factor(val)

        self.assertEqual(actualResult, expectedResult)

    def test_factor_2_2(self):
        val = 2
        expectedResult = [2]

        actualResult = Problem3.factor(val)

        self.assertEqual(actualResult, expectedResult)

    def test_factor_3_3(self):
        val = 3
        expectedResult = [3]

        actualResult = Problem3.factor(val)

        self.assertEqual(actualResult, expectedResult)

    def test_factor_4_2(self):
        val = 4
        expectedResult = [2]

        actualResult = Problem3.factor(val)

        self.assertEqual(actualResult, expectedResult)

    def test_factor_16_2(self):
        val = 16
        expectedResult = [2]

        actualResult = Problem3.factor(val)

        self.assertEqual(actualResult, expectedResult)

    def test_lpf_10_5(self):
        val = 10
        expectedResult = 5

        actualResult = Problem3.lpf(val)

        self.assertEqual(actualResult, expectedResult)

    def test_lpf_13195_29(self):
        val = 13195
        expectedResult = 29

        actualResult = Problem3.lpf(val)

        self.assertEqual(actualResult, expectedResult)

    def test_lpf_600851475143_6857(self):
        val = 600851475143
        expectedResult = 6857

        actualResult = Problem3.lpf(val)

        self.assertEqual(actualResult, expectedResult)

if __name__ == '__main__':
    unittest.main()
    