from problems import Problem014
import unittest

class test_problem014(unittest.TestCase):

    def test_longestCollatz_13_9(self):
        starting_val = 18
        expectedValue = 9

        actualValue = Problem014.longestCollatz(starting_val)
        self.assertEqual(expectedValue, actualValue)

'''
    def test_longestCollatz_1000000_837799(self):
        starting_val = 1000000
        expectedValue = 837799

        actualValue = Problem014.longestCollatz(starting_val)
        self.assertEqual(expectedValue, actualValue)
'''

if __name__ == '__main__':
    unittest.main()

