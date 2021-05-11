it = iter


def iter(*args):
    return it(args)

"""Дана целочисленная последовательность a, состоящая из нулей и единиц.
Выведите порядковый номер числа, с которого начинается первая самая
длинная группа одинаковых цифр,
идущих подряд. Одиночные элементы тоже считать группами."""


def seq28(a):
    digit = next(a)
    index = 1
    index_of_sequence = 1
    index_of_max_sequence = 1
    sequence_len = 1
    max_sequence_len = 1
    for i in a:
        index += 1
        if i == digit: # следующее число рано первому и последовательность увеличивается
            sequence_len += 1
        else:
            digit = i
            if sequence_len > max_sequence_len:
                max_sequence_len = sequence_len
                sequence_len = 1
                index_of_max_sequence = index_of_sequence
            index_of_sequence = index
    # index_of_max_sequence = index_of_sequence
    print(index_of_max_sequence)





# seq28(iter(0, 1, 0, 1))   # 1
seq28(iter(0, 1, 1, 1, 0))   # 2
# seq28(iter(1, 0, 1, 1))   # 3


"""Дана целочисленная последовательность a, состоящая из нулей и единиц. 
Выведите порядковый номер числа, с которого начинается последняя самая длинная группа 
одинаковых цифр, идущих подряд. Одиночные элементы тоже считать группами."""


def seq29(a):
    first = next(a)
    index = 1
    key_index = 1
    groop_index = {1: 1}
    for i in a:
        index += 1
        if i == first:
            groop_index[key_index] += 1
        else:
            key_index = index
            groop_index[key_index] = 1
        first = i
    sorted_tupl = sorted(groop_index.items(), key=lambda x: x[1])
    print(sorted_tupl[-1][0])


# seq29(iter(0, 1, 0, 1))   # 4
# seq29(iter(0, 1, 1, 1))   # 2
# seq29(iter(1, 0, 1, 1))   # 3
# seq29(iter(1, 1, 1, 0))   # 1