# https://stepik.org/lesson/21975/step/2?adaptive=true&unit=5235

lst = list(map(int, input().split()))
n = int(input())

rez = []
last_in = 0
if lst.count(n) > 0:
    for i in range(len(lst)):
        if lst[i] == n:
            rez.append(i)
    print(*rez)

else:
    print("None")


