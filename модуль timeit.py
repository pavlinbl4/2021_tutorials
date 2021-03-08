import timeit
start_time = timeit.default_timer()

def buble_sort(a:list)-> list:
    while True:
        flag = True
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i+1],a[i] = a[i],a[i+1]
                flag = False
        if flag == True:
            break


    return a
print(buble_sort([33,66,1,7,2 , 66,2,55,6,9,8888,1,4,6,8]))

print(timeit.default_timer() - start_time)
