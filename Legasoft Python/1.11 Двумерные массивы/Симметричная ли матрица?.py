n = int(input())
arr = [[0] * n] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))
flag = "YES"
for i in range(n):
    for j in range(n):
        if arr[i][j] != arr[j][i]:
            flag = "NO"
            break
print(flag)
