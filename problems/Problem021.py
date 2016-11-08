import math

def getProperDivisors(x):
    divisors = [1]
    for i in range(int(math.sqrt(x)), 1, -1):
        if x % i == 0:
            divisors.append(i)
            divisors.append(x//i)
    return divisors

def getAmicable(x):
    amicable = set()
    for i in range(2, x+1):
        sumProper = sum(getProperDivisors(i))
        sumCompliment = sum(getProperDivisors(sumProper))
        if sumCompliment == i and sumProper != sumCompliment:
            amicable.add(sumProper)
            amicable.add(sumCompliment)
    return amicable

if __name__ == '__main__':
    print("[Begin]")
    print("Proper :" , sum(getProperDivisors(220)))
    print("Amicable Sum:", sum(getAmicable(300)))
    print("Amicable Sum:", sum(getAmicable(10000)))
