n = int(input())
arr = []
ind = [0] * n
for i in range(n):
    arr.append(list(map(int, input().split())))
    ind[i] = sum(arr[i])
print(ind.index(max(ind)) + 1)
print(max(ind))
print(*arr[ind.index(max(ind))])



