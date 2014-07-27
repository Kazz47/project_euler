print "[Begin]"

def sumOfMultiples(maxVal):
    total = 0
    for x in range(0, maxVal):
        if (x % 3 == 0 or x % 5 == 0):
            total += x
    return total

if __name__ == '__main__':
    print "Total", sumOfMultiples(1000)