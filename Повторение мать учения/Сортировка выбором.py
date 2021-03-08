import timeit
start_time = timeit.default_timer()
arr = [5, 2, 9, 5, 7, 1]


def selection_sort(arr: list) -> list:
    while True:
        flag = True
        for i in range(len(arr) - 1):
            if arr[i + 1] < arr[i]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
                flag = False
        if flag == True:
            break
    return arr


print(selection_sort(arr))
print(timeit.default_timer() - start_time)


