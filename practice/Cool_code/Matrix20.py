# Matrix20
"""Дана матрица размера row * col.
Для каждого столбца матрицы найти произведение его элементов."""

row = 3
col = 5
arr = [[i + j * col for i in range(col)] for j in range(row)]
for i in arr:
    print('\t'.join(map(str, i)))
print("=" * 50)

for j in range(col):
    answer = 1
    for i in range(row):
        answer *= arr[i][j]
    print(answer)
