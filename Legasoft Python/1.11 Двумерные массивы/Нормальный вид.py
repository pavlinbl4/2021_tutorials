n, m = int(input()), int(input())
date = input().split()
for i in range(n):
    print(*date[(m * i):m * (1 + i)])
