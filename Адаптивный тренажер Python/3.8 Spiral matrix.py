# https://stepik.org/lesson/21976/step/1?adaptive=true&unit=5236

n = int(input())
a = []
count = 0
# создаю матрицу заполненную нулями или другим символом
for i in range(n):
    a.append(["0"] * n)

# заменяю нули по правилу
st = 0
while st < n//2+1:
    for i in range(n):
        if i == st:
            for j in range(st,n - st):# заполняем верхнюю строку
                count += 1
                a[i][j] = count
        elif st < i < n - 1 - st: #заполнем правый столбец
            count += 1
            a[i][n - 1 - st] = count
        elif i == n - 1 - st:  # заполняю нижнюю строку
            for j in range(n - 1 - st, -1 + st, -1):
                count += 1
                a[n - 1 - st][j] = count
    st = st + 1
    for i in range(n - 1 - st, st-1, - 1): # заполняем левый столбец снизу вверх
        count += 1
        a[i][st - 1] = count

for i in a:
    print(*i)






