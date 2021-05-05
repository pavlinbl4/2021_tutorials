# Matrix16
"""Дана квадратная матрица порядка ( M — нечетное число).
Начиная с элемента A11 и перемещаясь против часовой стрелки,
вывести все ее элементы по спирали: первый столбец,
последняя строка, последний столбец в обратном порядке,
первая строка в обратном порядке, оставшиеся элементы второго столбца и т. д.;
последним выводится центральный элемент матрицы."""

m = 5
arr = [[i + j * m for i in range(m)] for j in range(m)]
for i in arr:
    print("\t".join(map(str, i)))
print('=' * 50)
print('Matrix16')

for circle in range(m // 2 + 1):
    print("*" * 50)

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
    print()
