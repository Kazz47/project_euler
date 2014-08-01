from problems import Problem3

def equalList(values):
    for x in values:
        if (x != values[-1]):
            return False
    return True

def smallestMultipleBrutefoce(values):
    originalList = list(values)
    multipliers = [1] * len(values)

    while (not equalList(values)):
        minIndex = 0
        for i in range(1, len(values)):
            if (values[i] < values[minIndex]):
                minIndex = i
        multipliers[minIndex] += 1
        values[minIndex] = originalList[minIndex] * multipliers[minIndex]

    return values[0]

def smallestMultipleFactors(values):
    factorList = []
    factorCount = []
    for x in values:
        factors = Problem3.factor(x)
        for y in factors:
            if (y not in factorList):
                factorList.append(y)
                factorCount.append(factors.count(y))
            else:
                index = factorList.index(y)
                newCount = factors.count(y)
                oldCount = factorCount[index]
                if (newCount > oldCount):
                    factorCount[index] = newCount
    
    result = 1
    for i in range(0, len(factorList)):
        result *= pow(factorList[i], factorCount[i])
    return result

if __name__ == '__main__':
    print("[Begin]")
    print("Smallest Multiple:", smallestMultipleFactors(list(range(1, 21))))
    print("Smallest Multiple:", smallestMultipleBrutefoce([1234346144, 436412]))
