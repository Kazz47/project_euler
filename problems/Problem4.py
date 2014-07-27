print("[Begin]")

def isPalendrome(val):
    forward = str(val)
    reverse = forward[::-1]

    if (forward == reverse):
        return True
    return False

def largestPalendrome(pairOne, pairTwo):
    assert(len(pairOne) == 2 and len(pairTwo) == 2)
    largest = -1

    for x in range(pairOne[0], pairOne[1], -1):
        for y in range(pairTwo[0], pairTwo[1], -1):
            val = x * y
            if (isPalendrome(val) and val > largest):
                largest = val
    return largest

if __name__ == '__main__':
    print("Largest Palendrome:", largestPalendrome([999, 99], [999, 99]))
