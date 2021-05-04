"""Вывести элементы  k-го столбца данной матрицы.
"""
col = 5
row = 3
k = 4

# arr = [[i + j * col for i in range(col)] for j in range(row)]
arr = [[i + 1 for i in range(col)] for j in range(row)] # цифры в столбце соответствуют его номеру

for i in arr:
    print("\t".join(map(str, i)))

print("=" * 50)
j = k - 1  # если нумерация столбцов от единицы
for i in range(row):
    print(arr[i][j], end=' ')
