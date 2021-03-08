# https://stepik.org/lesson/21974/step/2?adaptive=true&unit=5234
n = int(input())
rez = []
for x in range(1,n+1):
    for i in range(x):
        rez.append(x)
print(rez[:n])
