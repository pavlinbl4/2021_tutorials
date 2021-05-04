# Matrix1
"""
Даны целые положительные числа m, n.
Сформировать целочисленную матрицу размера m*n,
у которой все элементы I строки имеют значение 10*i
"""


def create_matrix1(m, n):
    return [[j * 10 for i in range(m)] for j in range(n)]


print("Matrix1")
a = create_matrix1(3, 5)
for i in a:
    print(i)
print("=" * 50)
print()

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
print("=" * 50)
print()

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
print("=" * 50)
print()

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
    return [[i for i in arr]] * m


print("Matrix4")
a = create_matrix4(5, 3, [33, 17, 34])
for i in a:
    print(i)
print("=" * 50)
print()

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
print("=" * 50)
print()
