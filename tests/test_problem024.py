from problems.Problem024 import PermutationFinder
import unittest

class test_problem024(unittest.TestCase):

    def test_getFactoradic_463(self):
        finder = PermutationFinder()

        self.assertEqual([3,4,1,0,1,0], finder.getFactoradic(463));

    def test_permutationFinder_012(self):
        finder = PermutationFinder([0,1,2])

        self.assertEqual([1,2,0], finder.find(4));

    def test_permutationFinder_0123456789(self):
        finder = PermutationFinder([0,1,2,3,4,5,6,7,8,9])

        self.assertEqual([2,7,8,3,9,1,5,4,6,0], finder.find(1000000));

if __name__ == '__main__':
    unittest.main()
