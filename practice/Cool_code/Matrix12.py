"""Matrix12. Дана матрица размера .
Вывести ее элементы в следующем порядке: первый столбец сверху вниз,
второй столбец снизу вверх,
третий столбец сверху вниз, четвертый столбец снизу вверх и т. д."""
m = 3
n = 5
arr = [[i * n + j for j in range(n)] for i in range(m)]
for i in arr:
    print(i)
print("=" * 50)

for j in range(n):
    if j % 2 != 0:
        for i in range(m - 1, -1, -1):
            print(arr[i][j], end=' ')
    else:
        for i in range(m):
            print(arr[i][j], end=' ')
    print()



