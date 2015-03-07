from problems import Problem013
import unittest

class test_problem013(unittest.TestCase):

    def test_findFirstTriangleNumber_5_28(self):
        numbers = [1,2,3,4,5,6,7,8,9]
        expectedValue = 45

        actualValue = Problem013.sumList(numbers)
        self.assertEqual(expectedValue, actualValue)

if __name__ == '__main__':
    unittest.main()

