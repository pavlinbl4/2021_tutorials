import timeit

start_time = timeit.default_timer()

arr = [4, 2, 9, 3, 7, 1, 0, 77, 5]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr


print(insertion_sort(arr))
print(timeit.default_timer() - start_time)