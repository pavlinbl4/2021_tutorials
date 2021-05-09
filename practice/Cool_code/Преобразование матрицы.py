"""Matrix47.
Дана матрица размера col*row и целые числа k1 и k2.
Поменять местами строки матрицы с номерами k1 и k2 ."""

from random import randrange
row = 4
col = 5
k1 = 1
k2 = 4

arr = [[i + randrange(1,50)  + j  * col   for i in range(col)] for j in range(row)]
for i in arr:
    print('\t'.join(map(str,i)))
print("=" * 50)

print("Matrix47")
arr[k1 -1],arr[k2 - 1] = arr[k2 - 1], arr[k1 -1]
for i in arr:
    print("\t".join(map(str,i)))
print("=" * 50)

"""Matrix48.
Дана матрица размера col*row и целые числа k1 и k2.
Поменять местами строки столбцы  с номерами k1 и k2 ."""

print("Matrix48")
for j in range(k1):
    for i in range(row):
        arr[i][k1-1],arr[i][k2-1] = arr[i][k2-1],arr[i][k1-1]
for i in arr:
    print("\t".join(map(str,i)))
print("=" * 50)


