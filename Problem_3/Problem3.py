import math

print("[Begin]")

def isPrime(val):
    for x in range(int(math.sqrt(val)), 1, -1):
        if (val % x == 0):
            return False
    return True

def lpf(val):
    total = 0
    factors = factor(val)
    return factors[-1]

def factor(val):
    factors = []
    m = 2
    while (math.sqrt(m) < val):
        if (val % m == 0):
            val = val // m
            if (m not in factors):
                factors.append(m)
        else:
            m += 1
    return factors

if __name__ == '__main__':
    print("Largest Prime Factor:", lpf(600851475143))