# import timeit
#
# start_time = timeit.default_timer()
arr = [4, 2, 9, 3, 7, 1]

while True:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j] = key
            j -= 1

        # if arr[i] > arr[i+1]:
        #     arr[i],arr[i+1] = arr[i+1],arr[i]

print(arr)
