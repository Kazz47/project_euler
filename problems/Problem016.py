import math

def sumDigits(number):
    string = str(number)
    chars = list(string)
    sum = 0
    for x in chars:
        sum += int(x)
    return sum

def sumPower(x, y):
    val = 1
    for i in range(y):
        val *= x
    return sumDigits(val)

if __name__ == '__main__':
    print("[Begin]")
    print("Power Digit Sum:", sumPower(2,15))
    print("Power Digit Sum:", sumPower(2,1000))

