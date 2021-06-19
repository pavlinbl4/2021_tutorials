def decoration():
    print()
    print("=" * 50)
    print()


def answer(arr):
    for i in arr:
        print('\t'.join(map(str,i)))
    decoration()


arr = [[17, 3, -20, -12, 12], [9, 3, -23, 47, -43], [59, 3, -49, 25, 39], [49, 3, -28, 63, 38]]
row = 4
col = 5
k1 = 1
k2 = 4
print("input matrix")
answer(arr)


"""Matrix29. 
Дана матрица. В каждой ее строке найти количество элементов, 
меньших среднего арифметического всех элементов этой строки."""

def analize_matrix29(arr,row,col):
    print("Matrix29")
    average_in_row = [0] * row # список средних арифметических в каждой строке
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

def analize_matrix30(arr,row,col):
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