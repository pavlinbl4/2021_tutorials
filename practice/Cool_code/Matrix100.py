
m = 3
arr = [[j + i * m for j in range(m)] for i in range(m)]
print("input matrix")
for i in arr:
    print(i)
print("=" * 50)
#Matrix 96
print(end = '\n')
print("Matrix 96")
for i in range(m - 1):
    for j in range(m - 1):
        arr[j][m - i - 1],arr[m - i - 1][j] = arr[m - i - 1][j], arr[j][m - i - 1]
for i in arr:
    print(i)

# #Matrix 97
# print(end = '\n')
# print("Matrix 97")
# for i in range(m - 1):
#     for j in range(m - 1):
#         arr[i][j],arr[m - j - 1][m - i - 1] = arr[m - j - 1][m - i -1], arr[i][j]
# for i in arr:
#     print(i)

# #Matrix 98
# print(end = '\n')
# print("Matrix 98")
# for i in range(m - 1, -1, -1):
#     print()
#     for j in range(m - 1, -1, -1):
#         print(arr[i][j], end=" ")
# print()
#
#
# #Matrix 99
# print(end = '\n')
# print("Matrix 99")
# for j in range(m - 1, -1, -1):
#     print()
#     for i in range(m):
#         print(arr[i][j], end=" ")
#
# #Matrix 100
# print()
# print(end = '\n')
# print("Matrix 100")
# for j in range(m):
#     print()
#     for i in range(m - 1, -1, -1):
#         print(arr[i][j], end=" ")







