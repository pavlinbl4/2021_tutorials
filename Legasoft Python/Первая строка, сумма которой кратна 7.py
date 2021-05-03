# Здесь могла бы быть ваша функция
def find_line7(sp):
    for i in range(len(sp)):
        if sum(sp[i]) % 7 == 0:
            return i
    return -1


n = int(input())
sp = []
for i in range(n):
    sp.append([int(j) for j in input().split()])
F = find_line7(sp)
print(f"Сумма строки по номером {F + 1} кратна 7" if F != -1 else "Таких строк нет")