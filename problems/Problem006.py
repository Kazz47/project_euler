def sumOfSquares(values):
    total = 0
    for x in values:
        total += x * x
    return total

def squareOfSums(values):
    total = 0
    for x in values:
        total += x
    total = total * total
    return total

def sumDifference(values):
    return squareOfSums(values) - sumOfSquares(values)

if __name__ == '__main__':
    print("[Begin]")
    print("Difference of Sums:", sumDifference([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print("Difference of Sums:", sumDifference(list(range(1, 101))))
