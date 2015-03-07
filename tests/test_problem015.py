from problems import Problem015
import unittest

class test_problem015(unittest.TestCase):

    def test_numberPaths_2_2(self):
        x = 2
        y = 2
        expectedValue = 6

        actualValue = Problem015.numberPaths(x, y)
        self.assertEqual(expectedValue, actualValue)

    def test_longestCollatz_20_20(self):
        x = 20
        y = 20
        expectedValue = 137846528820

        actualValue = Problem015.numberPaths(x, y)
        self.assertEqual(expectedValue, actualValue)

if __name__ == '__main__':
    unittest.main()

