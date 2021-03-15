a = [2, 7, 15, 200]
b = [3, 4, 5, 6, 8, 11, 201]


def merge_lists(a, b: list) -> list:
    itog = []
    k = n = 0
    while k < len(a) and n < len(b):
        if a[k] < b[n]:
            itog.append(a[k])
            k += 1
        else:
            itog.append(b[n])
            n += 1
    if k < len(a):
        itog = itog + a[k:]
    if n < len(b):
        itog = itog + b[n:]
    print(itog)


merge_lists(a, b)
