d = {}
for _ in range(int(input())):
    a, b = input(), input()
    d[a], d[b] = b, a
print(d)