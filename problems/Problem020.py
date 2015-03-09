from problems import Problem016
import math

def sumFactorial(x):
    return Problem016.sumDigits(math.factorial(x))

if __name__ == '__main__':
    print("[Begin]")
    print("Factoral Digit Sum:", sumFactorial(15))
    print("Factoral  Digit Sum:", sumFactorial(100))

