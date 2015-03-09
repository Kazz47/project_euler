
def lenFib(x):
    counter = 2
    prev_val = 1
    val = 1
    while (len(str(val)) < x):
        temp = val
        val = prev_val + val
        prev_val = temp
        counter += 1
    return counter

if __name__ == '__main__':
    print("[Begin]")
    print("Length of Fib Number:", lenFib(3))
    print("Length of Fib Number:", lenFib(1000))

