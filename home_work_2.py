lst1 = [-22, 4, 7, 21, 22, 33, 36]
lst2 = [1, 4, 5, 9, 25]


def merge(lst1, lst2):
    rez = []
    while len(lst1) != 0 and len(lst2) != 0:
        if lst1[0] < lst2[0]:
            rez.append(lst1.pop(0))
        else:
            rez.append(lst2.pop(0))
    if lst1 != 0:
        rez = rez + lst1
    else:
        rez = rez + lst2
    return rez


print(merge(lst1, lst2))
