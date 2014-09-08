from problems import Problem011
import unittest

testGrid = [
        [8, 2, 22, 97, 38],
        [49, 49, 99, 40, 17],
        [81, 49, 31, 73, 55],
        [52, 70, 95, 23, 4],
        [22, 31, 16, 71, 51]
        ]

class test_problem011(unittest.TestCase):

    def test_searchVertical_4_6414210(self):
        listLength = 4;
        expectedResult = 6514520;

        actualResult = Problem011.searchVertical(testGrid, listLength)

        self.assertEqual(actualResult, expectedResult)

    def test_searchHorizontal_4_9507960(self):
        listLength = 4;
        expectedResult = 9507960;

        actualResult = Problem011.searchHorizontal(testGrid, listLength)

        self.assertEqual(actualResult, expectedResult)

    def test_searchDiagonalTLBR_4_9507960(self):
        listLength = 4;
        expectedResult = 16194745;

        actualResult = Problem011.searchDiagonalTLBR(testGrid, listLength)

        self.assertEqual(actualResult, expectedResult)

    def test_searchDiagonalBLTR_4_9585576(self):
        listLength = 4;
        expectedResult = 24468444;

        actualResult = Problem011.searchDiagonalBLTR(testGrid, listLength)

        self.assertEqual(actualResult, expectedResult)

if __name__ == '__main__':
    unittest.main()

