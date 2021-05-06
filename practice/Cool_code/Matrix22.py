# Matrix22
"""Дана матрица размера .
Для каждого столбца матрицы с четным номером найти сумму его элементов.
Условный оператор не использовать."""
row = 3
col = 5
arr = [[i + j * col for i in range(col)] for j in range(row)]
for i in arr:
    print('\t'.join(map(str,i)))
print("=" * 50)

for j in range(1,col,2):
    answer = 0
    for i in range(row):
        answer += arr[i][j]
    print(f'нумерацию столбцов начинаем с 1 - {answer}')