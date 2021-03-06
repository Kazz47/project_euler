from problems.Problem024 import PermutationFinder
import unittest

class test_problem024(unittest.TestCase):

    def test_getFactoradic_463(self):
        self.assertEqual([3,4,1,0,1,0], PermutationFinder.getFactoradic(463));

    def test_permutationFinder_012(self):
        finder = PermutationFinder([0,1,2])

        self.assertEqual([1,2,0], finder.find(4));

    def test_permutationFinder_throwOutOfBounds(self):
        finder = PermutationFinder([0,1,2])
        with self.assertRaises(ValueError):
            finder.find(7); # Only 6 permutations

    def test_permutationFinder_twoFromSameObject(self):
        finder = PermutationFinder([0,1,2])

        self.assertEqual([1,2,0], finder.find(4));
        self.assertEqual([2,0,1], finder.find(5));

    def test_permutationFinder_0123456789(self):
        finder = PermutationFinder([0,1,2,3,4,5,6,7,8,9])

        self.assertEqual([2,7,8,3,9,1,5,4,6,0], finder.find(1000000));

if __name__ == '__main__':
    unittest.main()
