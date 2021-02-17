# ввод информации
# str, col = map(int, input().split())
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

# str = 5
# col = 6
# table = [['.', '.', '.', 'X', 'X', '.'], ['.', 'X', 'X', '.', '.', '.'], ['.', '.', 'X', '.', '.', '.'], ['X', 'X', '.', '.', '.', '.'], ['X', '.', '.', 'X', 'X', '.']]
str,col = 2, 2
table = [['X', 'X'], ['X', 'X']]

def dead(table,i,j,count):
    if count == 3:
        table[i][j] = 'X'
def live(table, i, j,count):
    if count < 2 or count > 3:
        table[i][j] = '.'


def test(table,i,j):
    count = 0
    for x in range(-1,2):
        for y in range(-1,2):
            new_str = i + x
            new_col = j + y
            if new_str == -1:
                new_str = str-1
            if new_str == str:
                new_str = 0
            if new_col == -1:
                new_col = col-1
            if new_col == col:
                new_col = 0
            if table[new_str][new_col] == ".":
                count += 1

    if table[i][j] == "X":
        live(table, i, j,count)
    else:
        dead(table, i, j,count)

    print(f"test block {i}:{j}")
    for w in table:
        print(w)
    print("-"*40)




for i in range(str):
    for j in range(col):
            test(table,i,j)


# for i in table:
#     print(i)

