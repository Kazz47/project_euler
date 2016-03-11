from problems import Problem019
import unittest

class test_problem019(unittest.TestCase):

    def test_canGetNumDaysJan(self):
        expectedDays = 31
        days = Problem019.getNumDays(Problem019.Months.JAN, 2000)

        self.assertEqual(expectedDays, days)

    def test_canGetNumDaysFeb_nonLeap(self):
        expectedDays = 28
        days = Problem019.getNumDays(Problem019.Months.FEB, 1901)

        self.assertEqual(expectedDays, days)

    def test_canGetNumDaysFeb_Leap(self):
        expectedDays = 29
        days = Problem019.getNumDays(Problem019.Months.FEB, 1904)

        self.assertEqual(expectedDays, days)

    def test_canGetNumDaysFeb_centuryNonLeap(self):
        expectedDays = 28
        days = Problem019.getNumDays(Problem019.Months.FEB, 1900)

        self.assertEqual(expectedDays, days)

    def test_canGetNumDaysFeb_century400Leap(self):
        expectedDays = 29
        days = Problem019.getNumDays(Problem019.Months.FEB, 2000)

        self.assertEqual(expectedDays, days)

    def test_canGetNumDaysMar(self):
        expectedDays = 31
        days = Problem019.getNumDays(Problem019.Months.MAR, 2000)

        self.assertEqual(expectedDays, days)

    def test_canGetNumDaysApr(self):
        expectedDays = 30
        days = Problem019.getNumDays(Problem019.Months.APR, 2000)

        self.assertEqual(expectedDays, days)

    def test_canGetNumDaysMay(self):
        expectedDays = 31
        days = Problem019.getNumDays(Problem019.Months.MAY, 2000)

        self.assertEqual(expectedDays, days)

    def test_canGetNumDaysJun(self):
        expectedDays = 30
        days = Problem019.getNumDays(Problem019.Months.JUN, 2000)

        self.assertEqual(expectedDays, days)

    def test_canGetNumDaysJul(self):
        expectedDays = 31
        days = Problem019.getNumDays(Problem019.Months.JUL, 2000)

        self.assertEqual(expectedDays, days)

    def test_canGetNumDaysAug(self):
        expectedDays = 31
        days = Problem019.getNumDays(Problem019.Months.AUG, 2000)

        self.assertEqual(expectedDays, days)

    def test_canGetNumDaysSep(self):
        expectedDays = 30
        days = Problem019.getNumDays(Problem019.Months.SEP, 2000)

        self.assertEqual(expectedDays, days)

    def test_canGetNumDaysOct(self):
        expectedDays = 31
        days = Problem019.getNumDays(Problem019.Months.OCT, 2000)

        self.assertEqual(expectedDays, days)

    def test_canGetNumDaysNov(self):
        expectedDays = 30
        days = Problem019.getNumDays(Problem019.Months.NOV, 2000)

        self.assertEqual(expectedDays, days)

    def test_canGetNumDaysDec(self):
        expectedDays = 31
        days = Problem019.getNumDays(Problem019.Months.DEC, 2000)

        self.assertEqual(expectedDays, days)

    def test_1901_2000(self):
        expectedValue = 171
        value = Problem019.countFirstSundays(1901, 2000)
        self.assertEqual(expectedValue, value)

if __name__ == '__main__':
    unittest.main()
