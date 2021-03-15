import timeit

a = [4, 2, 9, 3, 7, 1, 0, 77, 5]


def is_sorted(b):
    for i in range(len(b) - 1):
        if b[i] >= b[i + 1]:
            return False
    return True


def buble_sort_1() -> list:
    while not is_sorted(a):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i + 1], a[i] = a[i], a[i + 1]
    return a


def buble_sort_2() -> list:
    while True:
        flag = True
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i + 1], a[i] = a[i], a[i + 1]
                flag = False
        if flag == True:
            break

    return a


print(a)
buble_sort_2()
print(a)
print(timeit.timeit(buble_sort_1, number=1000000))
print(timeit.timeit(buble_sort_2, number=1000000))
