from problems import Problem5
import unittest

class test_problem5(unittest.TestCase):

    def test_smallestMultiple(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expectedResult = 2520

        actualResult = Problem5.smallestMultipleFactors(values)

        for x in values:
            self.assertEqual(actualResult % x, 0)
        self.assertEqual(actualResult, expectedResult)

    def test_smallestMultiple(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        expectedResult = 232792560

        actualResult = Problem5.smallestMultipleFactors(values)

        for x in values:
            self.assertEqual(actualResult % x, 0)
        self.assertEqual(actualResult, expectedResult)


if __name__ == '__main__':
    unittest.main()
