a = [1, 2, 5, 99]
b = "dorww"
c = [99, 55, 66, 88]
# print(list(zip(a,b,c)))
# print(list(zip(a,c)))
# print(dict(zip(b, c)))
print(list(zip(a,c)))

arr1 = list(map(float,input().split()))
arr2 = list(map(float,input().split()))
print(*list(zip(arr1,arr2)))
print([sum(v) for v in zip(arr1,arr2)])