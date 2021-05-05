n = 5
lst = [[0] * n for i in range(n)]
i, j, di, dj = 0, 0, 1, 0
for k in range(n * n):
    lst[i][j] = k + 1
    if lst[(i + di) % n][(j + dj) % n]:
        di, dj = -dj, di
    i, j = i + di, j + dj
for line in lst:
    print(*line)