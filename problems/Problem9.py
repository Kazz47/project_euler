def isTriplet(a, b, c):
    if (a <= b and b <= c):
        sqrA = a * a;
        sqrB = b * b;
        sqrC = c * c;
        if (sqrA + sqrB == sqrC):
            return True
    return False

def productOfTripletWithSum(tripletSum):
    for x in range(1, tripletSum - 1): # Ends at tripletSum - 2
        remainingVal = tripletSum
        a = x
        remainingVal -= x
        for y in range(x, remainingVal): # Ends at tripletSum - 1
            b = y
            c = remainingVal - y
            if (isTriplet(a, b, c)):
                # print(a, b, c, "=", a + b + c)
                return a * b * c
    
    return None

if __name__ == '__main__':
    print("[Begin]")
    print("Product:", productOfTripletWithSum(12))
    print("Product:", productOfTripletWithSum(1000))
