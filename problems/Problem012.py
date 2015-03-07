from problems import Problem003

# Find the first triangle number with a given number of divisors
def findFirstTriangleNumber(target_divisors):
    num_divisors = 0
    counter = 0
    triangle_number = 0

    while (num_divisors < target_divisors):
        counter += 1
        triangle_number += counter
        factors = Problem003.factor(triangle_number)

        count_list = []
        current_index = -1;
        prev_val = None
        for x in factors:
            if (prev_val == x):
                count_list[current_index] += 1
            else:
                current_index += 1
                count_list.append(1)
                prev_val = x

        num_divisors = 1
        for x in count_list:
            num_divisors *= x+1

    return triangle_number

if __name__ == '__main__':
    print("[Begin]")
    print("Frist Triangle Number:", findFirstTriangleNumber(500))

