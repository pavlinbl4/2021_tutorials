"""Дана матрица размера M * N .
Вывести ее элементы, расположенные в столбцах с нечетными (четными) номерами .
Вывод элементов производить по столбцам, условный оператор не использовать."""
m = 3
n = 5
arr = [[i * n + j for j in range(n)] for i in range(m)]
for i in arr:
    print(i)
print("=" * 50)

for i in range(m):
    for j in range(1,n,2):
        print(arr[i][j], end = ' ')

print(end="\n")
print("=" * 50)

for i in range(m):
    for j in range(0,n,2):
        print(arr[i][j], end = ' ')

