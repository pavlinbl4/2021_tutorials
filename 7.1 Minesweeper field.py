#7.1 Minesweeper field
# ввод данных
n, m =map(int, input().split())
sea = []
for i in range(n):
    line = list(input())
    sea.append(line)

def find_mine(sea,i,j):
    count = 0
    for x in range(-1,2):
        for y in range(-1,2):
            index_i = i + x
            index_j = j + y
            # if 0 <= i+x < n and 0 <= j+x < n and 0 <= i+y < m and 0 <= j+y < m:
            if 0 <= index_i < n and 0 <= index_j < m  and sea[index_i][index_j] == "*":
                # if sea[i+x][j+y] == "*":
                count += 1
    sea[i][j] = count

# тестовый ввод данных
# n = 4
# m = 4
# sea = [['.', '.', '*', '.'], ['*', '*', '.', '.'], ['.', '.', '*', '.'], ['.', '.', '.', '.']]
# for i in sea:
#     print(*i)

# 1. прохожу по массиву в поиске полей без мин, нужные поля отправляю на проверку
for i in range(n):
    for j in range(m):
        if sea[i][j] == ".":
            find_mine(sea,i,j)
for i in sea:
    print("".join(map(str,i)))





