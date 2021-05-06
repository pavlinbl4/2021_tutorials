# Matrix19
"""Дана матрица размера .
Для каждой строки матрицы найти сумму ее элементов."""

row = 3
col = 5
k = 3
arr = [[j + i * col for j in range(col)] for i in range(row)]
for i in arr:
    print("\t".join(map(str, i)))
print("+" * 50)
for i in arr:
    print(sum(i))
