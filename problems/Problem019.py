from enum import Enum, IntEnum

class Months(Enum):
    JAN = 1
    FEB = 2
    MAR = 3
    APR = 4
    MAY = 5
    JUN = 6
    JUL = 7
    AUG = 8
    SEP = 9
    OCT = 10
    NOV = 11
    DEC = 12

class Days(IntEnum):
    SUN = 0
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6

def getNumDays(month, year):
    if month == Months.JAN:
        return 31
    elif month == Months.FEB:
        # Get leap years
        # Every four years except on centuries, unless divisible by 400.
        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            return 29
        else:
            return 28
    elif month == Months.MAR:
        return 31
    elif month == Months.APR:
        return 30
    elif month == Months.MAY:
        return 31
    elif month == Months.JUN:
        return 30
    elif month == Months.JUL:
        return 31
    elif month == Months.AUG:
        return 31
    elif month == Months.SEP:
        return 30
    elif month == Months.OCT:
        return 31
    elif month == Months.NOV:
        return 30
    elif month == Months.DEC:
        return 31

def countFirstSundays(startYear, endYear):
    currentDay = Days.TUE
    firstSundays = 0
    for year in range(startYear, endYear+1):
        for month in Months:
            currentDay += getNumDays(month, year)
            if currentDay % 7 == Days.SUN:
                firstSundays += 1
    return firstSundays

if __name__ == '__main__':
    print("[Begin]")
    print("Sundays fell on the 1st of the month in the 20th century:", countFirstSundays(1901, 2000))
