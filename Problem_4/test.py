import unittest
import Problem4

class Problem4Tests(unittest.TestCase):

    def test_isPalendrome_0_true(self):
        val = 0
        expectedResult = True

        actualResult = Problem4.isPalendrome(val)

        self.assertEqual(actualResult, expectedResult)


    def test_isPalendrome_10_false(self):
        val = 10
        expectedResult = False

        actualResult = Problem4.isPalendrome(val)

        self.assertEqual(actualResult, expectedResult)


    def test_largestPalendrome_twoDigits_9009(self):
        pairOne = [99, 9]
        pairTwo = [99, 9]
        expectedResult = 9009

        actualResult = Problem4.largestPalendrome(pairOne, pairTwo)

        self.assertEqual(actualResult, expectedResult)
        
    def test_largestPalendrome_threeDigits_906609(self):
        pairOne = [999, 99]
        pairTwo = [999, 99]
        expectedResult = 906609

        actualResult = Problem4.largestPalendrome(pairOne, pairTwo)

        self.assertEqual(actualResult, expectedResult)

if __name__ == '__main__':
    unittest.main()
    