from problems import Problem003

def findPrime(primeIndex):
    pos = 1
    index = 1
    while (index <= primeIndex):
        pos += 1
        if (Problem003.isPrime(pos)):
            index += 1

    return pos

if __name__ == '__main__':
    print("[Begin]")
    print("Prime Num:", findPrime(6))
    print("Prime Num:", findPrime(10001))
