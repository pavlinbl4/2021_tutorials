"""Вывести ее элементы в следующем порядке:
первая строка слева направо, вторая строка справа налево,
третья строка слева направо, четвертая строка справа налево и т. д."""
m = 3
n = 5
arr = [[i * n + j for j in range(n)] for i in range(m)]
for i in arr:
    print(i)
print("=" * 50)

flag = 1
for i in range(m):
    print(arr[i][:: 1 * flag])
    flag *= -1

print("=" * 50)

flag = 1
for j in range(n):
    print()
    for i in range(m):
        print(arr[i][j], end = ' ')
        flag *= -1