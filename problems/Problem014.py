
def collatzSequence(number):
    list = []
    list.append(number)
    while(number > 1):
        if (number % 2 == 0):
            number = number//2
        else:
            number = (3 * number) + 1
        list.append(number)
    return list


def longestCollatz(starting_val):
    end_val = starting_val//2
    max_size = 0
    max_start_val = 0
    while (starting_val > end_val):
        if (starting_val % 2 == 0):
            starting_val -= 1
        seq = collatzSequence(starting_val)
        size = len(seq)
        if (size > max_size):
            max_size = size
            max_start_val = starting_val
        starting_val -= 1

    return max_start_val

if __name__ == '__main__':
    print("[Begin]")
    print("Longest Collatz:", longestCollatz(1000000))

