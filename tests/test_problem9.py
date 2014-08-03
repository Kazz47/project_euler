from problems import Problem9
import unittest

class test_problem9(unittest.TestCase):
    
    def test_productOfTripletWithSum_3_1(self):
        tripletSum = 3
        expectedResult = 1

        actualResult = Problem9.productOfTripletWithSum(tripletSum)

        self.assertEqual(actualResult, expectedResult)
        
    def test_productOfTripletWithSum_12_60(self):
        tripletSum = 12
        expectedResult = 60

        actualResult = Problem9.productOfTripletWithSum(tripletSum)

        self.assertEqual(actualResult, expectedResult)
        
    def test_productOfTripletWithSum_1000_31875000(self):
        tripletSum = 1000
        expectedResult = 31875000

        actualResult = Problem9.productOfTripletWithSum(tripletSum)

        self.assertEqual(actualResult, expectedResult)

if __name__ == '__main__':
    unittest.main()
