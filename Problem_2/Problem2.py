print "[Begin]"

def fibonacciSum(mod, maxVal):
    total = 0
    fibValPrev = 1;
    fibVal = 1;
    while (fibVal < maxVal):
        if (fibVal % mod == 0):
            total += fibVal
        nextVal = fibValPrev + fibVal
        fibValPrev = fibVal
        fibVal = nextVal
    return total

if __name__ == '__main__':
    print "Total", fibonacciSum(2, 4000000)