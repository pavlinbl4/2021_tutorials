# https://stepik.org/lesson/22778/step/1?adaptive=true&unit=5351

# ввод информации
# st, col = map(int, input().split())
# # col = int(input())
# table = []
# for i in range(str):
#     table.append(list(input()))
#
# for i in table:
#     print(i)
# print(table)
# print()
# print("*"*100)
# print()

st = 5
col = 6
table = [['.', '.', '.', 'X', 'X', '.'], ['.', 'X', 'X', '.', '.', '.'], ['.', '.', 'X', '.', '.', '.'], ['X', 'X', '.', '.', '.', '.'], ['X', '.', '.', 'X', 'X', '.']]
# Точка "." обозначает мёртвую клетку, символ "X" − живую.

"""Распределение живых клеток в начале игры называется первым поколением. 
Каждое следующее поколение рассчитывается на основе предыдущего по таким правилам:
в пустой (мёртвой) клетке, рядом с которой ровно три живые клетки, зарождается жизнь;
если у живой клетки есть две или три живые соседки, то эта клетка продолжает жить;
в противном случае, если соседей меньше двух или больше трёх,
клетка умирает («от одиночества» или «от перенаселённости»)"""


def test(table, i, j):
    count = 0
    for x in range(-i, i+2):
        for y in range(-i, i+2):
            print(f'{table[x%col][y%st]} -> {x%col} -> {y%st}')
            if table[i][j] == table[x%col][y%st]:
                count += 1
    print(f"count = {count}")
    return count



for i in range(1):#st
    # print()
    for j in range(1):#col
        test(table, i, j)
        print(f" {table[i][j]} -> i ={i}, j = {j} ")

