# 1. Функция count_element(2,[1,8,9,2,5,2,2]) -> 3, подсчитывает кол-во элементов массива равных первому аргументу
def count_element(x, lst):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count


print(count_element(2, [1, 2, 9, 2, 5, 2, 2]))


# 2. Функция equal_elements([2,2,2,2]) -> True, возвращает истину если все элементы массива одинаковы, ложь, если хотя бы один элемент не равен остальным
def equal_elements(lst):
    flag = True
    for i in lst:
        if lst[0] != i:
            flag = False
    return flag


print(equal_elements([2, 2, 2, 2]))

# 3. Функция merge([2,5,9],[1,4,8]) -> [1,2,4,5,8,9], сливающая два отсортированных массива так, чтобы результриующий массив был отсортирован.
def merge(lst1,lst2):
    rez = []
    l = 0
    if len(lst1) >= len(lst2):
        l = len(lst2)
    else:
        l = len(lst1)



print(merge([2,5,9],[1,4,8]))

# 4. Функция is_sorted([3,7,9]) -> True, если массив отсортирован по возрастанию, False в противном случае.
def is_sorted(lst):
    flag = True
    for i in range(1, len(lst) - 1):
        if lst[i + 1] > lst[i]:
            flag = True
        else:
            flag = False
    return flag


print(is_sorted([113, 17, 9]))


# 5. Функция max([3,7,9,4]) -> 9 возвращает максимальный элемент массива.
def max(lst):
    max_digit = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_digit:
            max_digit = lst[i]
    return max_digit


print(max([3, 7, 9, 4]))
