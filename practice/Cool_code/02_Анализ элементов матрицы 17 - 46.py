def decoration():
    print()
    print("=" * 50)
    print()


def start_matrix(row, col):
    return [[i + j * col for i in range(col)] for j in range(row)]


row = 3
col = 5
arr = start_matrix(row, col)
arr = [[99, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]

print("исходная матрица")
for i in arr:
    print('\t'.join(map(str, i)))
print("*" * 50)
print()
print(arr)

# Matrix17
"""Дана матрица размера row * col и целое число  K.
Найти сумму и произведение элементов K-й строки данной матрицы."""

k = 3

print("Matrix17")
print(f"сумма элементов К строки - {sum(arr[k - 1])}")
pr = 1
for i in range(col):
    pr *= arr[k - 1][i]
print(f"произведение элементов К строки - {pr}")
decoration()

# Matrix18
"""Дана матрица размера col * row и целое число K.
Найти сумму и произведение элементов  K -го столбца данной матрицы."""

k = 3
print("Matrix18")
pr = 1
sm = 0
for i in range(row):
    pr *= arr[i][k - 1]
    sm += arr[i][k - 1]
print(f'сумма элементов столбца - {sm}')
print(f'произведение элементов столбца - {pr}')
decoration()

# Matrix19
"""Дана матрица размера .
Для каждой строки матрицы найти сумму ее элементов."""
print("Matrix19")
for i in arr:
    print(sum(i))
decoration()

# Matrix20
"""Дана матрица размера row * col.
Для каждого столбца матрицы найти произведение его элементов."""
print("Matrix20")
for j in range(col):
    answer = 1
    for i in range(row):
        answer *= arr[i][j]
    print(answer)
decoration()

# Matrix21
"""Дана матрица размера .
Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.
Условный оператор не использовать."""
print("Matrix21")
for i in range(0, row, 2):
    print(sum(arr[i]) / len(arr[i]))
decoration()

# Matrix22
"""Дана матрица размера .
Для каждого столбца матрицы с четным номером найти сумму его элементов.
Условный оператор не использовать."""
print("Matrix22")
for j in range(1, col, 2):
    answer = 0
    for i in range(row):
        answer += arr[i][j]
    print(f'нумерацию столбцов начинаем с 1 - {answer}')
decoration()

# Matrix23
"""
Дана матрица размера .
В каждой строке матрицы найти минимальный элемент.
"""
print("Matrix23")
for i in arr:
    print(min(i))
decoration()

# Matrix24
""" Дана матрица размера . 
В каждом столбце матрицы найти максимальный элемент."""
print("Matrix24")
for j in range(col):
    test = [0] * row
    for i in range(row):
        test[i] = arr[i][j]
    print(max(test))
decoration()

# Matrix25
""" Дана матрица размера . 
Найти номер ее строки с наибольшей суммой элементов и вывести данный номер, 
а также значение наибольшей суммы."""
print("Matrix25")
biggest = sum(arr[0])
biggest_index = 0
for i in range(1, row):
    if sum(arr[i]) > biggest:
        biggest = sum(arr[i])
        biggest_index = i
print(f"номер строки ( если начинаем отсчет с 1) - {biggest_index + 1}, значение суммы - {biggest}")
decoration()


# Matrix26.
"""Дана матрица. Найти номер ее столбца с наименьшим произведением элементов и вывести данный номер, 
а также значение наименьшего произведения."""
print("Matrix26")
answer = {}

for j in range(col):
    pr = 1
    for i in range(row):
        pr *= arr[i][j]
        answer[j + 1] = pr
sorte_tupl = max(answer.items(), key = lambda item:item[1])
print(f'номер столбца - {sorte_tupl[0]}')
print(f'произведение элементов столбца - {sorte_tupl[1]}')

