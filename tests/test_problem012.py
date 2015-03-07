from problems import Problem012
import unittest

class test_problem012(unittest.TestCase):

    def test_findFirstTriangleNumber_5_28(self):
        divisors = 5
        expectedValue = 28

        actualValue = Problem012.findFirstTriangleNumber(divisors)
        self.assertEqual(expectedValue, actualValue)

'''
    def test_findFirstTriangleNumber_500_76576500(self):
        divisors = 500
        expectedValue = 76576500

        actualValue = Problem012.findFirstTriangleNumber(divisors)
        self.assertEqual(expectedValue, actualValue)
'''

if __name__ == '__main__':
    unittest.main()

