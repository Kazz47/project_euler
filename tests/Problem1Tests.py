import unittest
import Problem1

class Problem1Tests(unittest.TestCase):
    
    def test_sumOfMultiples_10_24(self):
        maxVal = 10
        expectedValue = 23

        actualValue = Problem1.sumOfMultiples(maxVal)
        self.assertEqual(expectedValue, actualValue)

if __name__ == '__main__':
    unittest.main()