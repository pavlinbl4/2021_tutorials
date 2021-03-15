import timeit

start_time = timeit.default_timer()
arr = [4, 2, 9, 3, 7, 1, 0, 77, 5]


def selection_sort(nums):
    # значение i соответствует тому, сколько значений было отсортировано
    for i in range(len(nums)): # предполагаем, что первый элемент несортированного сегмента является наименьшим
        lowest_value_index = i
        for j in range(i + 1, len(nums)):         #  цикл перебирает несортированные элементы
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]         # Поменять местами значения самого низкого несортированного элемента с первым несортированным


selection_sort(arr)
print(arr)
print(timeit.default_timer() - start_time)

