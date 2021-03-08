# https://stepik.org/lesson/247716/step/8?unit=220169

# lst =list(map(int, input().split(" ")))
# print(lst)
# lst = [1, 3, 2, 4]
# lst = []
lst = [7,2,11]


def digits(lst, rez ):
    if len(lst) == 0:
        return {}
    if len(lst) == 1:
        return {}, set(lst)
    else:
        # lst.pop(0)
        # print(f" lst after pop - {lst}")
        rez.append(set(lst))
        rez.append(set(lst[:1]))
        return  digits(lst[1:],rez)



print(digits(lst,rez = []))
