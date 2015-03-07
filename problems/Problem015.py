import math

def nCr(n, r):
    return math.factorial(n) / math.factorial(r) / math.factorial(n-r)

def numberPaths(x, y):
    return nCr(x+y, x)

if __name__ == '__main__':
    print("[Begin]")
    print("Lattice Paths:", numberPaths(20,20))

