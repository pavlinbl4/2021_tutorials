#Matrix18
"""Дана матрица размера col * row и целое число K.
Найти сумму и произведение элементов  K -го столбца данной матрицы."""
row = 3
col = 5
k = 3
arr = [[j + i * col for j in range(col)] for i in range(row)]
for i in arr:
    print("\t".join(map(str,i)))
print("+" * 50)
pr = 1
sm = 0
for i in range(row):
    pr *= arr[i][k - 1]
    sm += arr[i][k - 1]
print(sm)
print(pr)


