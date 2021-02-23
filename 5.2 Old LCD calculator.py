# https://stepik.org/lesson/21306/step/1?adaptive=true&unit=5109
# n = input()
lst = list(map( int,list(input())))


line = " -- "
rt = "   |"
lt = "|   "
tt = "|  |"
ey = "    "
# digits = input()
digit = {0: [line, tt, tt, ey, tt, tt, line],
         1: [ey, rt, rt, ey, rt, rt, ey],
         2: [line, rt, rt, line, lt, lt, line],
         3: [line, rt, rt, line, rt, rt, line],
         4: [ey, tt, tt, line, rt,  rt, ey],
         5: [line, lt, lt, line, rt, rt, line],
         6: [line, lt, lt, line, tt,  tt, line],
         7: [line, rt, rt, ey, rt, rt, ey],
         8: [line, tt, tt, line, tt,  tt, line],
         9: [line, tt, tt, line, rt,  rt, line]}

print(f"x{'-' * (len(lst)*5-1)}x")
# for x in range(len(lst)):
for x in range(len(lst)):
    for i in range(7):

        print(f"|{ digit[lst[x]][i] }|")
    # print(f"|{digit[lst[0]][i]} {digit[lst[1]][i]} {digit[2][i]}"
    #       f"{digit[3][i]} {digit[4][i]} {digit[5][i]}"
    #       f"{digit[6][i]} {digit[7][i]} {digit[8][i]}"
    #       f"{digit[9][i]}|")
    # print(f"|{ digit[lst[0]][i] } |")


print(f"x{'-' * (len(lst)*5-1)}x")
