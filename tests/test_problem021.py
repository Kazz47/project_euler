from problems import Problem021
import unittest

class test_problem021(unittest.TestCase):

    def test_sumAmicable_10000_(self):
        x = 10000
        expectedValue = 31626

        actualValue = sum(Problem021.getAmicable(x))
        self.assertEqual(expectedValue, actualValue)

if __name__ == '__main__':
    unittest.main()
