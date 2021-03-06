it = iter


def iter(*args):
    return it(args)


"""Дана целочисленная последовательность a.
Выведите все элементы последовательности."""


def seq1(a):
    for i in a:
        print(i)


# seq1(iter(4, 1, 2))     # 4
# seq1(iter(777))         # 777
# seq1(iter(-1, -2, -3))  # -1


"""Дана целочисленная последовательность a. Выведите сумму её элементов."""


def seq2(a):
    s = 0
    for i in a:
        s += i
    print(s)


# seq2(iter(4, -1, 2))  # 5
# seq2(iter(777))  # 777
# seq2(iter(-1, -2, -3))  # -6


"""Дана целочисленная последовательность a. 
Выведите среднее арифметическое из её элементов."""


def seq3(a):
    s = 0
    count = 0
    for i in a:
        count += 1
        s += i
    print(s / count)


# seq3(iter(4, 2, 6))   # 4
# seq3(iter(4, 3, -1))   # 2
# seq3(iter(7, 1, 1, 1))   # 2.5


"""Дана целочисленная последовательность a. 
Выведите наибольший из её элементов."""


def seq4(a):  # начало домашнего задания
    # print(max(a))  # если можно использовать max - то все просто

    max_number = next(a)
    for i in a:
        if i > max_number:
            max_number = i
    print(max_number)


# seq4(iter(4, 2, 6))  # 6
# seq4(iter(-4, -3))  # -3
# seq4(iter(7, 1, 1))  # 7

"""Дана целочисленная последовательность a. 
Выведите порядковый номер первого из наименьших её элементов."""


# Задача_5
def seq5(a):
    min_digit = next(a)
    count = 1
    digit_number = 1
    for i in a:
        count += 1
        if i < min_digit:
            min_digit = i
            digit_number = count
    print(digit_number)


# seq5(iter(4, 5, 1, 6, 7))  # 3
# seq5(iter(-3, -4))  # 2
# seq5(iter(3, 7, 3))  # 1


"""Дана целочисленная последовательность a. 
Выведите порядковый номер последнего из наибольших её элементов."""


def seq6(a):
    max_number = next(a)
    count = 1
    flag = 1
    for i in a:
        count += 1
        if i >= max_number:  # если просто ">"  то первое  максимальное значение
            max_number = i
            flag = count
    print(flag)


# seq6(iter(4, 5, 1, 6))   # 4
# seq6(iter(-3, -4))   # 1
# seq6(iter(3, 7, 3, 7))   # 4


"""Дана целочисленная последовательность a. 
Есть ли в ней хотя бы одно отрицательное число?"""


def seq7(a):  # тут и без next  все было решено
    for i in a:
        if i < 0:
            print(True)
            return
    print(False)


# seq7(iter(4, 5, 1, 6))  # false
# seq7(iter(-3, -4))  # true
# seq7(iter(3, 7, -3, 7))  # true

"""Дана целочисленная последовательность a. 
Упорядочена ли она по возрастанию?"""


def seq8(a):
    min_number = next(a)
    for i in a:
        if i <= min_number:
            print("False")
            return
        else:
            min_number = i
    print("True")


# seq8(iter(1, 4, 5, 10))
# seq8(iter(3, 4, 5, 4))
# seq8(iter(3, 3, 4))   # есть недопонимание теории, если два элемента одинаковы, то последовательность не упорядочена по возрастанию?
# seq8(iter(-3, -2, -1))


"""Дана целочисленная последовательность a. 
Упорядочена ли она по невозрастанию?"""


def seq9(a):
    max_number = next(a)
    for i in a:
        if i > max_number:
            print("False")
            return
        else:
            max_number = i
    print("True")


# seq9(iter(10, 5, 4, 1))  # true
# seq9(iter(4, 3, 2, 3))  # false
# seq9(iter(4, 3, 3))  # true аналогичный вопрос с одинаковыми числами в последовательности
# seq9(iter(-3, -2, -1))  # false


"""Дана целочисленная последовательность a. 
Сколько в ней элементов, меньших своего правого соседа?"""


def seq10(a):
    left = next(a)
    count = 0
    for i in a:
        if i > left:
            count += 1
        left = i
    print(count)


# seq10(iter(4,7,9))  # 2
# seq10(iter(-3, -2, -4))   # 1
# seq10(iter(10,))   # 0


"""Дана целочисленная последовательность a. 
Является ли каждый второй элемент положительным?"""


def seq11(a):
    first = next(a)
    count = 1
    for i in a:
        count += 1
        if i <= 0 and count % 2 == 0:
            print(False)
            return
    print(True)


# seq11(iter(-4, 7, -9))  #
# seq11(iter(-3, 2, -4, -2))   #
# seq11(iter(10, 10))   #


"""Дана целочисленная последовательность a. 
Предположим, что есть некая последовательность b, которая является накопительной суммой a. 
То есть, b_1 = a_1, b_2 = a_1 + a_2, b_3 = a_1 + a_2 + a_3 и т. д. 
Найдите сумму элементов последовательности b."""


def seq12(a):
    s = 0
    pred = 0
    for i in a:
        pred += i
        s += pred
    print(s)


# seq12(iter(2, 2, 3))
# seq12(iter(3, 2, 1))
# seq12(iter(1, 1, 1, 1))


"""
Дана целочисленная последовательность a. 
Если брать только каждый второй элемент, получится возрастающая последовательность?
"""


def seq13(a):
    first = next(a)
    max_digit = next(a)
    count = 1
    for i in a:
        if count % 2 == 0:
            if i <= max_digit:
                print(False)
                return
            max_digit = i
        count += 1
    print(True)


# seq13(iter(-4, 7, -9))  #
# seq13(iter(-3, 2, -4, -2))  #
# seq13(iter(-1, 3, -2, 7, -3))  #
# seq13(iter(-1, 3, -2, 7, -3, 5))  #

"""Дана целочисленная последовательность a. 
Если брать только каждый второй элемент, начиная с первого, 
получится невозрастающая последовательность?"""


def seq14(a):
    first = next(a)
    min_digit = next(a)
    count = 1
    for i in a:
        if count % 2 == 0:
            if i > min_digit:
                print(False)
                return
            min_digit = i
        count += 1
    print(True)


# seq14(iter(-1, 3, 0, 7, -3))  # true
# seq14(iter(5, 2, 2))   # true
# seq14(iter(-1, 3, 0, 7, -3))   # false
# seq14(iter(1, 3, 0, 7, 2))   # false


"""Дана целочисленная последовательность a. 
Найдите сумму элементов, меняя знак каждого второго элемента."""


def seq15(a):
    count = 1
    s = 0
    for i in a:
        if count % 2 == 0:
            i *= -1
        s += i
        count += 1
    print(s)


# seq15(iter(1, -1, 1))   # 3
# seq15(iter(5, 2, 2))   # 5
# seq15(iter(-1, 3, 0, 7, -3))   # -14


"""Дана целочисленная последовательность a. 
Найдите количество положительных и неположительных чисел."""


def seq16(a):
    neg_count = 0
    pos_count = 0
    for i in a:
        if i > 0:
            pos_count += 1
        else:
            neg_count += 1
    print(pos_count, neg_count)


# seq16(iter(1, -1, 1))   # 2 1
# seq16(iter(5, 2, 2))   # 3 0
# seq16(iter(-1, 3, 0, 7, -3))   # 2 3


"""Дана целочисленная последовательность a. 
Найдите порядковый номер первого чётного числа. Если таких чисел нет, выведите 0."""


def seq17(a):
    index = 0
    for i in a:
        index += 1
        if i % 2 == 0:
            print(index)
            return
    print(0)


# seq17((5, 2, 4))   # 2
# seq17((2, 6, 4, 8))   # 1
# seq17((7, 3, 1))   # 0


"""Дана целочисленная последовательность a. 
Найдите сумму порядковых номеров чётных элементов. Если таких нет, выведите 0."""


def seq18(a):
    summ = 0
    index = 0
    for i in a:
        index += 1
        if i % 2 == 0:
            summ += index
    print(summ)


# seq18(iter(1, 2, 4))   # 5
# seq18(iter(2, 6, 4, 8))   # 10
# seq18(iter(7, 3, 1))   # 0


"""Дана целочисленная последовательность a. 
Найдите сумму порядковых номеров нечётных элементов и сумму самих этих элементов. 
Если таких нет, выведите два нуля."""


def seq19(a):
    summ = 0
    summ_index = 0
    index = 0
    for i in a:
        index += 1
        if i % 2 != 0:
            summ_index += index
            summ += i
    print(summ_index, summ)


# seq19(iter(1, 2, 4))   # 1 1
# seq19(iter(7, 3, 1))   # 6 11
# seq19(iter(2, 6, 4, 8))   # 0 0


"""Дана последовательность a, состоящая из пар чисел (каждая пара - массив длины 2). 
Выведите первую пару, у которой максимальная сумма."""


def seq20(a):
    max_para = next(a)
    max_sum = sum(max_para)
    for i in a:
        if sum(i) > max_sum:
            max_sum = sum(i)
            max_para = i
    print(max_para)


# seq20(iter([1, 1], [0, 3], [2, 1]))  # [0, 3]
# seq20(iter([-1, 1], [0, 0], [-2, 0]))   # [-1, 1]
# seq20(iter([5, 10]))   # [5, 10]


"""Дана последовательность a, состоящая из пар чисел (каждая пара - массив длины 2). 
Числа в паре - стороны прямоугольника. Выведите минимальную площадь прямоугольника."""


def seq21(a):
    min_para = next(a)
    min_sq = min_para[0] * min_para[1]
    for i in a:
        if i[0] * i[1] < min_sq:
            min_sq = i[0] * i[1]
    print(min_sq)


# seq21(iter([1, 3], [3, 1], [2, 1]))  # 2
# seq21(iter([5, 5], [3, 4], [4, 4]))   # 12
# seq21(iter([5, 3]))   # 15


"""Дана последовательность a, состоящая из пар чисел (каждая пара - массив длины 2). 
Числа в паре - стороны прямоугольника. Выведите максимальный периметр прямоугольника."""


def seq22(a):
    max_para = next(a)
    for i in a:
        if sum(i) > sum(max_para):
            max_para = i
    print(sum(max_para) * 2)


# seq22(iter([1, 3], [3, 1], [2, 1]))   # 8
# seq22(iter([5, 5], [3, 4], [4, 4]))   # 20
# seq22(iter([5, 3]))   # 16


"""
Дана целочисленная последовательность a. 
Выведите два наибольших элемента в порядке невозрастания.
"""


def seq23(a):
    max_1 = next(a)
    max_2 = next(a)
    if max_2 > max_1:
        max_1, max_2 = max_2, max_1
    for i in a:
        if i >= max_1:
            max_2 = max_1
            max_1 = i
    print(max_1, max_2)


# seq23(iter(3, 1, 5, 2))   # 5 3
# seq23(iter(-1, -2, -3, -4))   # -1 -2
# seq23(iter(4, 5, 3, 5))   # 5 5


"""Дана целочисленная последовательность a. 
Выведите наибольшую сумму двух соседних элементов."""


def seq24(a):
    zero = next(a)
    first = next(a)
    max_sum = zero + first
    for i in a:
        sum_neighbour = first + i
        first = i
        if sum_neighbour > max_sum:
            max_sum = sum_neighbour
    print(max_sum)


# seq24(iter(3, 2, 5, 1))   # 7
# seq24(iter(-1, -2, -3, -4))   # -3
# seq24(iter(3, 5, 4, 6))   # 10


"""Дана целочисленная последовательность a, состоящая из нулей и единиц. 
Выведите количество подряд идущих нулей для каждой серии из нулей, 
и количество подряд идущих единиц для каждой серии из единиц."""


def seq25(a):
    first = next(a)
    zero_count = one_count = 1

    for i in a:
        if first != i:
            print(zero_count if i == 1 else one_count)
            zero_count = one_count = 1
        else:
            if i == 0:
                zero_count += 1
            else:
                one_count += 1
        first = i
    print(zero_count if i == 0 else one_count)


# seq25(iter(0, 1, 0, 1))
# seq25(iter(1, 1, 1, 0))
# seq25(iter(0, 0, 1, 1))


"""Дана целочисленная последовательность a, состоящая из нулей и единиц. 
Выведите количество групп одинаковых цифр, идущих подряд. 
Одиночные элементы тоже считать группами."""


def seq26(a):
    first = next(a)
    count = 1
    for i in a:
        if first != i:
            count += 1
        first = i
    print(count)


# seq26(iter(0, 1, 0, 1))   # 4
# seq26(iter(1, 1, 1, 0))   # 2
# seq26(iter(0, 0, 0, 0))   # 1


"""Дана целочисленная последовательность a, состоящая из нулей и единиц. 
Выведите длину самой большой группы одинаковых цифр, идущих подряд. 
Одиночные элементы тоже считать группами."""


def seq27(a):
    first = next(a)
    max_count = 1
    count = 1
    for i in a:
        if i == first:
            count += 1
        else:
            if count > max_count:
                max_count = count
                count = 1
        first = i
    print(max(max_count, count))


# seq27(iter(0, 1, 0, 1))   # 1
# seq27(iter(1, 1, 1, 0))   # 3
# seq27(iter(0, 0, 0, 0))   # 4


"""Дана целочисленная последовательность a, состоящая из нулей и единиц. 
Выведите порядковый номер числа, с которого начинается первая самая 
длинная группа одинаковых цифр, 
идущих подряд. Одиночные элементы тоже считать группами."""


def seq28(a):
    first = next(a)
    index = 1
    key_index = 1
    groop_index = {1:1}
    for i in a:
        index += 1
        if i == first:
            groop_index[key_index] += 1
        else:
            key_index = index
            groop_index[key_index] = 1
        first = i
    sorted_tupl = max(groop_index.items(),key= lambda x:x[1])
    print(sorted_tupl[0])






# seq28(iter(0, 1, 0, 1))   # 1
# seq28(iter(0, 1, 1, 1, 0))   # 2
# seq28(iter(1, 0, 1, 1))   # 3


"""Дана целочисленная последовательность a, состоящая из нулей и единиц. 
Выведите порядковый номер числа, с которого начинается последняя самая длинная группа 
одинаковых цифр, идущих подряд. Одиночные элементы тоже считать группами."""


def seq29(a):
    sum_digit = next(a)


# seq29(iter(0, 1, 0, 1))   # 4
# seq29(iter(0, 1, 1, 1))   # 2
# seq29(iter(1, 0, 1, 1))   # 3
# seq29(iter(1, 1, 1, 0))   # 1


"""Дана целочисленная последовательность a. 
Проверьте, соблюдается ли закономерность, что второе и каждое следующее число равно 
сумме всех предыдущих элементов. Если соблюдается, выведите 0, 
а если нет - порядковый номер первого элемента, нарушающего закономерность."""


def seq30(a):
    index = 1
    all_befor = next(a)
    for i in a:
        index += 1
        if i != all_befor:
            print(index)
            return
        else:
            all_befor += i
    print(0)


# seq30(iter(3, 3, 6, 12))   # 0
# seq30(iter(0, 0, 0, 0))   # 0
# seq30(iter(1, 1, 1, 1))   # 3


"""Дана целочисленная последовательность a. 
Проверьте, соблюдается ли закономерность, что третье и каждое следующее число равно 
сумме двух предыдущих элементов. 
Если соблюдается, выведите 0, а если нет - порядковый номер первого элемента, 
нарушающего закономерность."""


def seq31(a):
    first = next(a)
    second = next(a)
    index = 3
    for i in a:
        if i != second + first:
            print(index)
            return
        else:
            first = second
            second = i
        index += 1
    print(0)





# seq31(iter(1, 1, 2, 3, 5))   # 0
# seq31(iter(5, 6, 11, 17, 18))   # 5
# seq31(iter(1, 1, 1, 1))   # 3


"""Дана целочисленная последовательность a. 
Верно ли, что сумма всех элементов с чётными 
номерами равна сумме элементов с нечётными номерами?"""


def seq32(a):
    even = 0
    odd = 0
    count = 1
    for i in a:
        if count % 2 == 0:
            even += i
        else:
            odd += i
        count += 1
    print(odd == even)


# seq32(iter(1, 1, 2, 7, 5))   # true
# seq32(iter(2, 3, 2, 3, 2))   # true
# seq32(iter(1, 1, 1, 1, 1))   # false


"""Дана упорядоченная по невозрастанию целочисленная последовательность a и целое число k. 
Найдите количество чисел, которые больше, либо равны элементу последовательности с номером k, 
и при этом больше 0."""


def seq33(a, k):  # что-то много переменных создал
    index = 0
    count = 0
    k_digit = 0
    for i in a:
        index += 1
        if i > 0:
            count += 1
        if index == k:
            k_digit = i
            for j in a:
                if j == k_digit and j > 0:
                    count += 1
    print(count)



# seq33(iter(10, 9, 8, 7, 7, 7, 5, 5), 5)   # 6
# seq33(iter(3, 2, 1, 0, 0), 5)   # 3
# seq33(iter(0, 0, 0, 0), 2) # 0

