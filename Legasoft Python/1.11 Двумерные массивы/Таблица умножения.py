n,m = int(input()),int(input())
for x in range(1,n + 1):
    print(*[i * x for i in range(1,m + 1)])


arr = [[i * x for i in range(1,m + 1)] for x in range(1,n + 1)]
for i in range(n):
    print(*arr[i])