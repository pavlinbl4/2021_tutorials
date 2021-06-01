def decoration():
    print()
    print("=" * 50)
    print()

# Matrix1
"""
Даны целые положительные числа m, n.
Сформировать целочисленную матрицу размера m*n,
у которой все элементы I строки имеют значение 10*i
"""


def create_matrix1(m, n):
    return [[j * 10 for i in range(1, m + 1)] for j in range(1, n + 1)]


print("Matrix1")
a = create_matrix1(3, 5)
for i in a:
    print(i)
decoration()

# Matrix2
"""
Даны целые положительные числа m, n.
Сформировать целочисленную матрицу размера m*n,
у которой все элементы J столбца имеют значение 5*i
"""


def create_matrix2(m, n):
    return [[i * 5 for i in range(m)] for j in range(n)]


print("Matrix2")
a = create_matrix2(3, 5)
for i in a:
    print(i)
decoration()

# Matrix3
"""
Даны целые положительные числа m, n  и набор
из m чисел
Сформировать целочисленную матрицу размера m*n,
у которой в каждом столбце содержатся все числа 
из исходного набора (в том же порядке)
"""


def create_matrix3(m, n, arr):
    # a = [0] * m
    # for i in range(m):
    #     a[i] = [arr[i]] * n
    # return a

    return [[arr[i]] * n for i in range(m)]


print("Matrix3")
a = create_matrix3(3, 5, [77, 55, 99])
for i in a:
    print(i)
decoration()

# Matrix4
"""
Даны целые положительные числа m, n  и набор
из n чисел
Сформировать целочисленную матрицу размера m*n,
у которой в каждой строке содержатся все числа 
из исходного набора (в том же порядке)
"""


def create_matrix4(m, n, arr):
    # return [arr] * m
    # return [[i for i in arr]] * m
    return [arr[:] for _ in range(m)]


print("Matrix4")
b = [33, 17, 34]
a = create_matrix4(5, 3, b)
for i in a:
    print(i)
decoration()

# Matrix5
"""
Даны целые положительные числа m, n.
Число d  и набор из n чисел
у которой первый столбец совпадает с исходным набором чисел, 
а элементы каждого следующего столбца равны сумме 
соответствующего элемента предыдущего столбца и числа d
"""


def create_matrix5(row, col, d, arr):
    return [[arr[i] + d * j for j in range(col)] for i in range(row)]


print("Matrix5")
a = create_matrix5(5, 3, 4, [33, 17, 64, 55, 74])
for i in a:
    print(i)
decoration()

# Matrix8
"""Вывести элементы  k-го столбца данной матрицы.
"""


def create_matrix8(row, col, k):
    return [[i + 1 for i in range(col)] for j in range(row)]  # цифры в столбце соответствуют его номеру


print("Matrix8")
row = 3
col = 6
k = 4
arr = create_matrix8(row, col, k)
for i in arr:
    print(i[k])
decoration()

# Matrix9
"""Дана матрица размера M * N .
Вывести ее элементы, расположенные в столбцах с четными номерами .
Вывод элементов производить по столбцам, условный оператор не использовать."""

print("Matrix9")
row = 3
col = 6
k = 4
arr = create_matrix8(row, col, k)
# for i in arr: # исходная матрица
#     print(i)
for j in range(1, col, 2):
    for i in range(row):
        print(arr[i][j], end=' ')

decoration()

# Matrix10
"""Дана матрица размера M * N .
Вывести ее элементы, расположенные в столбцах с нечетными номерами .
Вывод элементов производить по столбцам, условный оператор не использовать."""

print("Matrix10")
row = 3
col = 6
k = 4
arr = create_matrix8(row, col, k)
for j in range(0, col, 2):
    for i in range(row):
        print(arr[i][j], end=' ')
decoration()

# Matrix11 в данном решении рассматривается выод значений готовой матрицы , а не генерация матрицы заполняемой змейкой
"""Вывести ее элементы в следующем порядке:
первая строка слева направо, вторая строка справа налево,
третья строка слева направо, четвертая строка справа налево и т. д."""


def create_matrix11(m, n):
    return [[j + i * n - 2 for j in range(1, n + 1)] for i in range(1, m + 1)]


m = 3
n = 4
print("Matrix11")
arr = create_matrix11(m, n)
print(arr)
flag = 1
for i in range(m):
    print(*arr[i][:: 1 * flag])
    flag *= -1
decoration()

# Matrix12
"""Дана матрица размера .
Вывести ее элементы в следующем порядке: первый столбец сверху вниз,
второй столбец снизу вверх,
третий столбец сверху вниз, четвертый столбец снизу вверх и т. д."""


def create_matrix12(m, n):
    return [[i * n + j for j in range(n)] for i in range(m)]


m = 3
n = 4
print("Matrix12")
arr = create_matrix12(m, n)
# print(arr)
for j in range(n):
    if j % 2 != 0:
        for i in range(m - 1, -1, -1):
            print(arr[i][j], end=' ')
    else:
        for i in range(m):
            print(arr[i][j], end=' ')
    print()
decoration()

# Matrix13
"""Дана квадратная матрица порядка .
Начиная с элемента , вывести ее элементы следующим образом («уголками»):
все элементы первой строки; элементы последнего столбца,
кроме первого (уже выведенного) элемента; оставшиеся элементы второй строки;
оставшиеся элементы предпоследнего столбца и т. д.; последним выводится элемент .
"""


def create_matrix13(m):
    return [[i + j * m for i in range(m)] for j in range(m)]


m = 4
arr = create_matrix13(m)

print("исходная матрица для задач 13 - 14 - 15 - 16")
for i in arr:
    print("\t".join(map(str, i)))
print("=" * 50)

print("Matrix13")
for x in range(m):
    for i in range(m - x):
        print(arr[x][i], end=' ')
    print("   ", end='')  # такой вариант вывода на мой взгляд нагляднее
    # print()
    for i in range(1 + x, m):
        print(arr[i][m - 1 - x], end=' ')
    print()
decoration()

# Matrix14

m = 4
arr = create_matrix13(m)
print("Matrix14")
for x in range(m):
    for i in range(m - x):
        print(arr[i][x], end=' ')
    print("    ", end='')
    for i in range(x + 1, m):
        print(arr[m - x - 1][i], end=' ')
    print()
decoration()

# Matrix15
m = 5
arr = create_matrix13(m)
print("Matrix15")
for circle in range(m // 2 + 1):
    # print("*" * 50)

    i = circle
    for j in range(circle, m - circle):
        print(arr[i][j], end=' ')
    print()

    j = m - 1 - circle
    for i in range(1 + circle, m - circle):
        print(arr[i][j], end=' ')
    print()

    i = m - 1 - circle
    for j in range(m - 2 - circle, -1 + circle, -1):
        print(arr[i][j], end=' ')
    print()

    j = circle
    for i in range(m - 2 - circle, circle, -1):
        print(arr[i][j], end=' ')
decoration()

# Matrix16
m = 5
arr = create_matrix13(m)
print("Matrix16")
for circle in range(m // 2 + 1):

    j = circle
    for i in range(circle, m - circle):
        print(arr[i][j], end=' ')
    print()

    i = m - 1 - circle
    for j in range(1 + circle, m - circle):
        print(arr[i][j], end=' ')
    print()

    j = m - 1 - circle
    for i in range(m - 2 - circle, -1 + circle, -1):
        print(arr[i][j], end=' ')
    print()

    i = circle
    for j in range(m - 2 - circle, circle, -1):
        print(arr[i][j], end=' ')
