from problems import Problem001
import unittest

class test_problem001(unittest.TestCase):

    def test_sumOfMultiples_10_24(self):
        maxVal = 10
        expectedValue = 23

        actualValue = Problem001.sumOfMultiples(maxVal)
        self.assertEqual(expectedValue, actualValue)

if __name__ == '__main__':
    unittest.main()

