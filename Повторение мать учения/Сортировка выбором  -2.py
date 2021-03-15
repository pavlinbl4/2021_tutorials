import timeit
start_time = timeit.default_timer()
arr = [4, 2, 9, 3, 7, 1, 0, 77, 5]


for i in range(len(arr) - 1):
   idx = i
   for j in range(i + 1, len(arr)):
       if arr[j] < arr[idx]:
           idx = j
   arr[i], arr[idx] = arr[idx], arr[i]
print(arr)
print(timeit.default_timer() - start_time)
