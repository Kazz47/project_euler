from problems import Problem003

def sumOfPrimes(targetIndex):
    sum = 0;
    for x in range(2, targetIndex): # Ends at targetIndex - 1
        if (Problem003.isPrime(x)):
            sum = sum + x;
    return sum

if __name__ == '__main__':
    print("[Begin]")
    print("Sum of Primes:", sumOfPrimes(12))
    print("Sum of Primes:", sumOfPrimes(2000000))

