# Matrix17
"""Дана матрица размера row * col и целое число  K.
Найти сумму и произведение элементов K-й строки данной матрицы."""
row = 3
col = 5
k = 2
arr = [[i + j * col for i in range(col)] for j in range(row)]
for i in arr:
    print('\t'.join(map(str,i)))
print("*" * 50)
print(f"сумма элементов К строки - {sum(arr[k - 1])}")
pr = 1
for i in range(col):
    pr *= arr[k - 1][i]
print(f"произведение элементов К строки - {pr}")
