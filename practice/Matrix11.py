m = 5
arr = [[i + j * m for i in range(m)] for j in range(m)]
for i in arr:
    print("\t".join(map(str, i)))
print("=" * 50)

for i in range(m):
    print()
    if i % 2 == 0:
        for j in range(m):
            print(arr[i][j], end=' ')
    else:
        for j in range(m - 1, -1, - 1):
            print(arr[i][j], end=' ')
