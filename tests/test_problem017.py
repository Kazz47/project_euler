from problems import Problem017
import unittest

class test_problem017(unittest.TestCase):

    def test_getSeriesStringSize_5_19(self):
        x = 5
        expectedValue = 19

        actualValue = Problem017.getSeriesStringSize(x)
        self.assertEqual(expectedValue, actualValue)

    def test_getNumberAsString_342_23(self):
        x = 342
        expectedValue = 23

        actualValue = len(Problem017.getNumberAsString(x))
        self.assertEqual(expectedValue, actualValue)

    def test_getNumberAsString_115_20(self):
        x = 115
        expectedValue = 20

        actualValue = len(Problem017.getNumberAsString(x))
        self.assertEqual(expectedValue, actualValue)

    def test_getSeriesStringSize_1000_21213(self):
        x = 1000
        expectedValue = 21124

        actualValue = Problem017.getSeriesStringSize(x)
        self.assertEqual(expectedValue, actualValue)

if __name__ == '__main__':
    unittest.main()

