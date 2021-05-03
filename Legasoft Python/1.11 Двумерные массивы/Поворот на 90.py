n, m = int(input()), int(input())
arr = [[0] * m] * n
for i in range(n):
    arr[i] = [int(x) for x in input().split()]
# answer = []
for j in range(m):
    # answer[j].append([])
    for i in range(n -1,-1,-1):
        print(arr[i][j], end=' ')
    print()
print()

    #     answer[j].append(arr[i][j])
