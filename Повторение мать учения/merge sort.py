def merge_sort(arr: list) -> list:
    if len(arr) == 1:
        return arr
    else:
        return arr[:len(arr) // 2], arr[len(arr) // 2:]


b = [100, 4, 5, 6, 8, 11, 201]


print(merge_sort(b))
