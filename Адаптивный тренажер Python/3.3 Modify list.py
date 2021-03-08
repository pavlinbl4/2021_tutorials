# https://stepik.org/lesson/21209/step/2?adaptive=true&unit=5095

def modify_list(l):
    # for x in range(len(l)-1,-1,-1):
    #     if l[x] % 2 != 0:
    #         l.remove(l[x])
    # for x in range(len(l)-1,-1,-1):
    #     l[x] = int(l[x] / 2)
    # return l
    for x in range(len(l)-1,-1,-1):
        if l[x] % 2 != 0:
            l.pop(x)
        else:
            l[x] = int(l[x]/2)


lst = [8,1,5,7,9,8,1,2,0]
modify_list(lst)
print(lst)
