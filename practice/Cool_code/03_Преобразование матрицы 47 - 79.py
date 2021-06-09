def decoration():
    print()
    print("=" * 50)
    print()


def answer(arr):
    for i in arr:
        print('\t'.join(map(str,i)))
    decoration()


arr = [[17, 3, 10, 42, 12], [9, 11, 23, 47, 43], [59, 18, 49, 25, 39], [49, 33, 28, 63, 38]]
row = 4
col = 5
k1 = 1
k2 = 4
print("input matrix")
answer(arr)

"""Matrix47.
Дана матрица размера col*row и целые числа k1 и k2.
Поменять местами строки матрицы с номерами k1 и k2 ."""


def transform_matrix_47(arr, row, col, k1, k2):
    print("Matrix47")
    arr[k1 - 1], arr[k2 - 1] = arr[k2 - 1], arr[k1 - 1]
    answer(arr)


# transform_matrix_47(arr, row, col, k1, k2)

"""Matrix48.
Дана матрица размера col*row и целые числа k1 и k2.
Поменять местами  столбцы  с номерами k1 и k2 ."""

def transform_matrix_48(arr, row, col, k1, k2):
    print("Matrix48")
    for j in range(k1):
        for i in range(row):
            arr[i][k1-1],arr[i][k2-1] = arr[i][k2-1],arr[i][k1-1]
    answer(arr)


# transform_matrix_48(arr, row, col, k1, k2)


"""Matrix49.
Дана матрица размера col*row.
Преобразовать матрицу, поменяв местами минимальный и максимальный элемент в каждой строке"""
def transform_matrix_49(arr, row, col):
    print("Matrix49")
    for i in arr:
        large = max(i)
        small = min(i)
        small_index = i.index(small)
        large_index = i.index(large)
        i[small_index],i[large_index] = i[large_index],i[small_index]
    answer(arr)


# transform_matrix_49(arr, row, col)

"""Matrix50.
Дана матрица размера col*row.
Преобразовать матрицу, поменяв местами минимальный и максимальный элемент в каждом столбце."""
def transform_matrix_50(arr, row, col):
    stolb = [0] * row
    for j in range(col):
        for i in range(row):
            stolb[i] = arr[i][j]
        i_large = stolb.index(max(stolb))
        i_small = stolb.index(min(stolb))
        arr[i_small][j], arr[i_large][j] = arr[i_large][j],arr[i_small][j]
    print("Matrix50")
    answer(arr)


# transform_matrix_50(arr, row, col)

"""Matrix51. 
Дана матрица размера col*row.
Поменять местами строки, содержащие минимальный и максимальный элементы матрицы.
"""
def transform_matrix_51(arr, row, col):
    max_digit = arr[0][0]
    min_digit = arr[0][0]
    for i in range(row):
        for j in range(col):
            if arr[i][j] > max_digit:
                max_digit = arr[i][j]
            if arr[i][j] < min_digit:
                min_digit = arr[i][j]
    print(max_digit, min_digit)
    for i in range(row):
        if min_digit in arr[i]:
            min_digit = i
        if max_digit in arr[i]:
            max_digit = i
    print(max_digit, min_digit)
    arr[min_digit], arr[max_digit] = arr[max_digit], arr[min_digit]
    print("Matrix51")
    answer(arr)


# transform_matrix_51(arr, row, col)

