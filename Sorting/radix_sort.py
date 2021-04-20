from functools import reduce

def __flatten(A):
    return reduce(lambda x, y: x + y, A)

def __get_num_digits(A):
    m = 0
    for item in A:
        m = max(m, item)
    return len(str(m))

def radix(A):
    num_digits = __get_num_digits(A)
    for digit in range(0, num_digits):
        B = [[] for i in range(10)]
        for item in A:
            # num is the bucket number that the item will be put into
            num = item // 10 ** (digit) % 10
            B[num].append(item)
        A = __flatten(B)
    return A


def main():
    A = [55, 45, 3, 289, 213, 1, 288, 53, 2]
    A = radix(A)
    print(A)
    
    B  = [i for i in range(1000000)]
    from random import shuffle
    shuffle(B)
    B = radix(B)
    print(B[:6], B[-6:])

main()