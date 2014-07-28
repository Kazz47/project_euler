from problems import Problem6
import unittest

class Problem6Tests(unittest.TestCase):

    def test_sumOfSquares_10_385(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expectedResult = 385

        actualResult = Problem6.sumOfSquares(values)

        self.assertEqual(actualResult, expectedResult)

    def test_squareOfSums_10_3025(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expectedResult = 3025

        actualResult = Problem6.squareOfSums(values)

        self.assertEqual(actualResult, expectedResult)

    def test_sumDifference_10_2640(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expectedResult = 2640

        actualResult = Problem6.sumDifference(values)

        self.assertEqual(actualResult, expectedResult)

    def test_sumDifference_100_25164150(self):
        values = list(range(1, 101))
        expectedResult = 25164150

        actualResult = Problem6.sumDifference(values)

        self.assertEqual(actualResult, expectedResult)


if __name__ == '__main__':
    unittest.main()
