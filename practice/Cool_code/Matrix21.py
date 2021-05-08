"""Matrix21. Дана матрица размера .
Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.
Условный оператор не использовать."""

m = 5
n = 6
arr = [[i * n + j for j in range(n)] for i in range(m)]
for i in arr:
    print(i)
print("=" * 50)

for i in range(0, m, 2):
    print(sum(arr[i])/len(arr[i]))