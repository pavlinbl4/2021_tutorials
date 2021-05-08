"""
Matrix23. Дана матрица размера .
В каждой строке матрицы найти минимальный элемент.
"""
row = 3
col = 5
arr = [[i + j * col for i in range(col)] for j in range(row)]
for i in arr:
    print('\t'.join(map(str,i)))
print("=" * 50)

for i in arr:
    print(min(i))