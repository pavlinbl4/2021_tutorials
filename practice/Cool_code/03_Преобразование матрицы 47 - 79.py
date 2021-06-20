def decoration():
    print()
    print("=" * 50)
    print()


def answer(arr):
    for i in arr:
        print('\t'.join(map(str,i)))
    decoration()


arr = [[17, 3, -10, -42, 12], [9, 11, -23, 47, -43], [59, 18, -49, 25, 39], [49, 33, -28, 63, 38]]
arr2 = [[17, 3, -10, -42, 12, 4], [9, 11, -23, 47, -43,5], [59, 18, -49, 25, 39,7], [49, 33, -28, 63, 38,8]]
row = 4
col = 5
col2 = 6
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

"""Matrix52. Дана матрица. 
Поменять местами столбцы, содержащие минимальный и максимальный элементы матрицы."""

def transform_matrix_52(arr, row, col):
    max_digit = arr[0][0]
    min_digit = arr[0][0]
    for i in range(row):
        for j in range(col):
            if arr[i][j] > max_digit:
                max_digit = arr[i][j]
            if arr[i][j] < min_digit:
                min_digit = arr[i][j]
    print("Matrix52")
    print(f'максимальное и минимальное значение в матрице {max_digit}, {min_digit}')
    for j in range(col):
        for i in range(row):
            if arr[i][j] == max_digit:
                max_digit = j
            if arr[i][j] == min_digit:
                min_digit = j
    print(f'номера столбцов для обмена {max_digit}, {min_digit}')
    for i in range(row):
        arr[i][min_digit],arr[i][max_digit] = arr[i][max_digit],arr[i][min_digit]
    answer(arr)

# transform_matrix_52(arr, row, col)

"""Matrix53. Дана матрица. 
Поменять местами столбец с номером 1 (для Pythone 0  как я понимаю) и последний из столбцов, 
содержащих только положительные элементы. Если требуемых столбцов нет, то вывести матрицу без изменений."""

def transform_matrix_53(arr, row, col):
    col_index = col - 1
    x= 0
    for j in range(col - 1, 0, -1):
        for i in range(row):
            if arr[i][j] < 0:
                col_index -= 1
                break
    if col_index != 0:
        for i in range(row):
            arr[i][0], arr[i][col_index] = arr[i][col_index], arr[i][0]
    print("Matrix53")
    answer(arr)

# transform_matrix_53(arr, row, col)

"""Matrix54. Дана матрица. 
Поменять местами столбец с номером K и первый из столбцов, 
содержащих только отрицательные элементы. 
Если требуемых столбцов нет, то вывести матрицу без изменений."""

def transform_matrix_54(arr, row, col, k):
    negativ_col_index = 0 # индекс первого столбца который может содержать все отрицательные элементы
    for j in range(col):
        count = 0
        for i in range(row):
            if arr[i][j] >= 0:
                break
            else:
                negativ_col_index = j
                count += 1
        if count == row:
            print(negativ_col_index)
            for i in range(row):
                arr[i][k], arr[i][negativ_col_index] = arr[i][negativ_col_index], arr[i][k]


    print("Matrix54")
    answer(arr)


# transform_matrix_54(arr, row, col, 1)



"""Matrix55. 
Дана матрица размера (row — четное число). 
Поменять местами верхнюю и нижнюю половины матрицы."""


def transform_matrix_55(arr, row, col):
    half = int(row/2)
    for x in range(half):
        # arr[x],arr[row - x -1] = arr[row - x -1],arr[x] # меняем верхнюю с нижней, вторую с предпоследней
        arr[x], arr[half + x] = arr[half + x], arr[x] # замена именно половин
    print("Matrix55")
    answer(arr)

# transform_matrix_55(arr, row, col)


"""Matrix56.
Дана матрица размера ( col — четное число). Поменять местами левую и правую половины матрицы."""
def transform_matrix_56(arr2, row, col2):
    half = col2//2
    for i in range(row):
        for j in range(half):
            x = arr2[i][j]
            y = arr2[i][half + j]
            arr2[i][j],arr2[i][half + j] = arr2[i][half + j],arr2[i][j]


    print("Matrix56")
    answer(arr2)



# transform_matrix_56(arr2, row, col2) # для проверки в строке 21 изменить arr на arr2


"""Matrix57.
 Дана матрица размера (  col  row  — четные числа). Поменять местами левую верхнюю и правую нижнюю четверти матрицы."""




