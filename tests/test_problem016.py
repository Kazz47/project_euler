from problems import Problem016
import unittest

class test_problem016(unittest.TestCase):

    def test_sumPower_2_15(self):
        x = 2
        y = 15
        expectedValue = 26

        actualValue = Problem016.sumPower(x, y)
        self.assertEqual(expectedValue, actualValue)

    def test_sumPower_2_1000(self):
        x = 2
        y = 1000
        expectedValue = 1366

        actualValue = Problem016.sumPower(x, y)
        self.assertEqual(expectedValue, actualValue)

if __name__ == '__main__':
    unittest.main()

