"""
Matrix23. Дана матрица размера .
В каждой строке матрицы найти минимальный элемент.
"""
from random import randrange
row = 3
col = 5
arr = [[i + randrange(1,50)  + j  * col   for i in range(col)] for j in range(row)]
for i in arr:
    print('\t'.join(map(str,i)))
print("=" * 50)
print("Matrix23")
for i in arr:
    print(min(i))



"""
Matrix24. Дана матрица размера . 
В каждом столбце матрицы найти максимальный элемент."""
print("=" * 50)
print("Matrix24")
for j in range(col):
    test = [0] * row
    for i in range(row):
        test[i] = arr[i][j]
    print(max(test))

