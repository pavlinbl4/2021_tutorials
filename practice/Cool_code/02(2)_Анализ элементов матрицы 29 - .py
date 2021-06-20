import numpy as np


def decoration():
    print()
    print("=" * 50)
    print()


def answer(arr):
    for i in arr:
        print('\t'.join(map(str, i)))
    decoration()


arr = [[9, 3, -20, -12, 12], [9, 1, -23, 47, -43], [58, 4, -48, -26, 30], [49, 3, -28, 63, -38]]
row = 4
col = 5
k1 = 1
k2 = 4
print("input matrix")
answer(arr)

"""Matrix29. 
Дана матрица. В каждой ее строке найти количество элементов, 
меньших среднего арифметического всех элементов этой строки."""


def analize_matrix29(arr, row, col):
    print("Matrix29")
    average_in_row = [0] * row  # список средних арифметических в каждой строке
    for i in range(row):
        average_in_row[i] = sum(arr[i]) / col
    print(average_in_row)
    for i in range(row):
        count = 0
        for j in range(col):
            x = arr[i][j]
            if arr[i][j] < average_in_row[i]:
                count += 1
        print(f'Строка {i} - искомых элементов {count}')


# analize_matrix29(arr,row,col)


"""Matrix30. 
Дана матрица. 
В каждом ее столбце найти количество элементов, больших среднего арифметического всех элементов этого столбца."""


def analize_matrix30(arr, row, col):
    print("Matrix30")
    average_in_column = 0
    for j in range(col):
        col_elems = [0] * row
        for i in range(row):
            col_elems[i] = arr[i][j]
        average_in_column = sum(col_elems) / row
        count = 0
        for digit in col_elems:
            if digit > average_in_column:
                count += 1
        print(f' количество искомых элементов в столбце {j} - {count}')
        print(col_elems, average_in_column)


# analize_matrix30(arr,row,col)


"""Matrix31. Дана матрица. 
Найти номера строки и столбца для элемента матрицы, наиболее близкого к среднему значению всех ее элементов."""


def analize_matrix31(arr, row, col):
    print("Matrix31")
    sum_all_elements = 0
    for i in arr:
        sum_all_elements += sum(i)
    matrix_everage = sum_all_elements / (col * row)
    print(matrix_everage)

    # b = [elem for el in arr for elem in el]
    # matrix_everage = np.mean(b)

    answer = arr[0][0]
    answer_coordinate = [0, 0]
    for i in range(row):
        for j in range(col):
            if abs(arr[i][j] - matrix_everage) == 0:
                print(f'координаты искомого значения - {i} ,{j} ')
                break
            else:
                if abs((arr[i][j]) - matrix_everage) < answer:
                    answer = abs((arr[i][j]) - matrix_everage)
                    answer_coordinate = [i, j]

    print(answer_coordinate)


# analize_matrix31(arr,row,col)


"""Matrix32. 
Дана целочисленная матрица. Найти номер первой из ее строк, содержащих равное количество положительных и отрицательных элементов 
(нулевые элементы матрицы не учитываются). Если таких строк нет, то вывести 0."""


def analize_matrix32(arr, row, col):
    print("Matrix32")
    flag = 0
    for i in range(row):
        plus_elem = 0
        minus_elem = 0
        for j in range(col):
            x = arr[i][j]
            if arr[i][j] > 0:
                plus_elem += 1
            elif arr[i][j] < 0:
                minus_elem += 1
        if minus_elem == plus_elem:
            print(f'номер искомой строки {i}')
            flag = 1
            break
    if flag == 0:
        print(f'искомых строк не найденно, выводим {0}')


# analize_matrix32(arr, row, col)


"""Matrix33. 
Дана целочисленная матрица. 
Найти номер последнего из ее столбцов, содержащих равное количество положительных и отрицательных элементов 
(нулевые элементы матрицы не учитываются). Если таких столбцов нет, то вывести 0."""


def analize_matrix33(arr, row, col):
    print("Matrix33")
    flag = 0
    for j in range(col - 1, -1, -1):
        plus_elem = 0
        minus_elem = 0
        for i in range(row):
            if arr[i][j] > 0:
                plus_elem += 1
            elif arr[i][j] < 0:
                minus_elem += 1
        if minus_elem == plus_elem:
            print(f'номер искомого столбца {j}')
            flag = 1
            break
    if flag == 0:
        print(f'искомых столбцов не найденно, выводим {0}')


# analize_matrix33(arr, row, col)

"""Matrix34.
 Дана целочисленная матрица. Найти номер последней из ее строк, 
 содержащих только четные числа. Если таких строк нет, то вывести 0 ."""

def analize_matrix34(arr, row, col):
    print("Matrix34")
    flag = 0
    for i in range(row -1,-1,-1):
        count = 0
        for j in range(col):
            if arr[i][j]%2 == 0:
                count += 1
        if count == col:
            print(f'номер искомой строки {i}')
            flag = 1
            break
    if flag == 0:
        print(f'искомых строк не найденно, выводим {0}')

# analize_matrix34(arr, row, col)
