def array1(n):
    # print([0 for _ in range(n)])  # Local variable 'i' value is not used ??? как исправить ?
    print([0] * n)


# array1(0)
# array1(1)
# array1(3)


def array2(n):
    # print([i for i in range(n)])
    print(list(range(n)))


# array2(0)
# array2(1)
# array2(3)


def array3(n):
    # print([i for i in range(1, n + 1)])
    print(list(range(1, n + 1)))


# array3(0)
# array3(1)
# array3(3)


def array4(n):
    print([n] * n)


# array4(0)
# array4(1)
# array4(3)


def array5(n):
    print(list(range(n, 0, -1)))


# array5(0)
# array5(1)
# array5(3)


def array6(n):
    a = [0] * n
    for i in range(n):
        a[i] = n - i - 1
    print(a)
    # print(list(range(n - 1, -1, -1)))


# array6(0)
# array6(1)
# array6(3)


def array7(n, s):
    print([s] * n)


# array7(0, 'a')
# array7(1, 'a')
# array7(3, 'xyz')


def array8(n):
    # print([i * 2 for i in range(n)])
    print(list(range(0, n * 2, 2)))


# array8(0)
# array8(1)
# array8(3)


def array9(n):
    # print([i * 2 + 1 for i in range(n)])
    print(list(range(1, n * 2, 2)))


# array9(0)
# array9(1)
# array9(3)


def array10(n):
    print([i * 2 for i in range(1, n + 1)])


# array10(0)
# array10(1)
# array10(3)


def array11(x, y):
    print([i for i in range(x, y + 1)])


# array11(0, 1)
# array11(5, 7)
# array11(-2, 0)


def array12(x, y):
    print([i for i in range(y - 1, x, - 1)])


# array12(0, 1)
# array12(5, 7)
# array12(-2, 2)


""" Дано целое число n. Создайте и выведите массив, заполненный числами от 1 до n(включительно),
каждое число по два раза.
"""


def array13(n):  # list comprehension ?
    itog = [0] * (n * 2)
    for i in range(1, n + 1):
        for x in range((i - 1) * 2, i * 2):
            itog[x] = i

    print(itog)


# array13(1)
# array13(2)
# array13(5)

"""Дано целое число n. Создайте и выведите массив длины n,
в котором первое число 1, а каждое следующее больше на свой порядковый номер
"""


def array14(n):
    arr = [0] * n
    arr[0] = 1
    for i in range(1, n):
        arr[i] = arr[i - 1] + i + 1
    print(arr)


# array14(1)
# array14(3)
# array14(5)

"""Дано целое число n. Создайте и выведите массив длины n,
в котором первые два числа единицы, а каждое следующее - 
это сумма двух предыдущих (ряд Фибоначчи).
"""


def array15(n):
    arr = [0] * n
    arr[0] = arr[1] = 1
    for i in range(2,n):
        arr[i] = arr[i - 1] + arr[i - 2]
    print(arr)


#
# array15(2)
# array15(5)
# array15(7)

"""Дан целочисленный массив a. 
Измените этот массив, умножив каждое число в нём на 2. Выведите массив """



def array16(a):
    print([i * 2 for i in a])


# array16([])
# array16([1])
# array16([-2, 0, 5])

"""Дан целочисленный массив \(a\). 
Измените этот массив, умножив каждое второе число в нём на 2. Выведите массив"""



def array17(a):
    for i in range(1, len(a), 2):
        a[i] = a[i] * 2
    print(a)


# array17([])
# array17([1, 1, 1])
# array17([1, 2, 2, 1])

"""Дан целочисленный массив \(a\). 
Измените этот массив, умножив каждое второе число в нём, начиная с первого, на 2. 
Выведите массив \(a\)."""



def array18(a):
    for i in range(0, len(a), 2):
        a[i] = a[i] * 2
    print(a)


# array18([])
# array18([1, 1, 1])
# array18([1, 2, 2, 1])

"""Дан целочисленный массив \(a\). 
Измените этот массив, умножив каждое нечётное число в нём на 2. Выведите массив \(a\)."""
def array19(a):
    for i in range(len(a)):
        if a[i] % 2 != 0:
            a[i] = a[i] * 2
    print(a)


# array19([])
# array19([1, 1, 1])
# array19([1, 2, 3, 3])

"""Дан целочисленный массив \(a\). Измените этот массив, умножив каждое нечётное число в нём на 2, 
а каждое чётное разделив нацело на 2. Выведите массив \(a\)."""
def array20(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a[i] = a[i] // 2
        else:
            a[i] = a[i] * 2
    print(a)


# array20([])
# array20([1, 1, 2])
# array20([2, 4, 3, 5])

"""Дан целочисленный массив \(a\). Измените этот массив, заменив каждое отрицательное на 0. Выведите массив \(a\)."""
def array21(a):
    for i in range(len(a)):
        if a[i] < 0:
            a[i] = 0
    print(a)


#
# array21([])
# array21([-1, 1, 2])
# array21([-1, 2, 3, -4])

"""Дан целочисленный массив \(a\). Измените этот массив, 
заменив каждое отрицательное на противоположное положительное. Выведите массив \(a\)."""
def array22(a):
    for i in range(len(a)):
        if a[i] < 0:
            a[i] *= -1
    print(a)


# array22([])
# array22([-1, 1, 2])
# array22([1, 2, 1, 2])


"""Дан целочисленный массив \(a\). Измените этот массив, обнулив каждый элемент, 
который больше своего правого соседа. Выведите массив \(a\)."""
def array23(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            a[i] = 0
    print(a)


# array23([1, 2])
# array23([3, 2, 1])
# array23([1, 2, 1, 2])

"""Дан целочисленный массив \(a\). Измените этот массив, обнулив каждый элемент, 
который больше своего левого соседа. Выведите массив \(a\)."""
def array24(a):
    for i in range(len(a)-1, 0, -1):
        if a[i] > a[i - 1]:
            a[i] = 0
    print(a)


# array24([1, 2, 3, 4])
# array24([3, 2, 1, 0])
# array24([1, 3, 2, 4])

"""Дан целочисленный массив \(a\). Выведите каждое второе число из этого массива."""
def array25(a):
    for i in range(1, len(a), 2):
        print(a[i])


# array25([1, 2, 4, 3])
# array25([2, 3, 4])
# array25([1, 2, 3, 4, 5, 6])


def array26(a): # Дан целочисленный массив a. Выведите каждое чётное число из этого массива.
    # for i in range(len(a)):
    #     if a[i] % 2 == 0:
    #         print(a[i])
    for i in a:
        if i % 2 == 0:
            print(i)


# array26([1, 2, 4, 3])
# array26([2, 3, 4])
# array26([1, 2, 3, 4, 5, 6])

"""Дан целочисленный массив a. Выведите каждое число из этого массива, которое заканчивается на 4 или 7."""
def array27(a):
    for i in a:
        if i % 10 == 4 or i % 10 == 7:
            print(i)


# array27([41, 76, 0])
# array27([2, 3, 4])
# array27([4, 24, 107])

"""Дан целочисленный массив \(a\). Выведите каждое число из этого массива, которое не делится на 2 и 3"""
def array28(a):
    for i in a:
        if i % 2 != 0 and i % 3 != 0:
            print(i)


# array28([10, 9, 8])
# array28([2, 3, 4, 5, 6])
# array28([1, 5, 7, 9])

"""Дан целочисленный массив \(a\). 
Измените массив таким образом, чтобы каждый второй элемент обменялся местами с предыдущим. 
Выведите массив \(a\)."""


def array29(a):
    for i in range(1, len(a), 2):
        a[i], a[i - 1] = a[i - 1], a[i]
    print(a)



# array29([1, 2, 3, 4])
# array29([1, 2, 2, 1, 3])
# array29([1, 5, 7])

"""Дан целочисленный массив \(a\). 
Измените массив таким образом, чтобы элементы в нём встали в противоположном порядке (развернуть  массив задом наперёд). 
Выведите массив \(a\)."""


def array30(a):
    for i in range(len(a) // 2):
        a[i], a[-i - 1] = a[-i - 1], a[i]
    print(a)


# array30([1])
# array30([10, 20, 15])
# array30([5, 3, 7, 4])

"""ан целочисленный массив \(a\) чётной длины. 
Измените массив таким образом, чтобы левая и правая половины поменялись местами. 
Выведите массив \(a\)."""
def array31(a):
    l = int(len(a) / 2)
    for i in range(l):
        a[i],a[i + l] = a[i + l],a[i]
    print(a)


# array31([1, 2])
# array31([1, 2, 3, 4])
# array31([1, 2, 3, 3, 2, 1])

"""Дан целочисленный массив \(a\). 
Измените массив таким образом, чтобы каждый элемент сдвинулся вправо на одну позицию, 
а последний элемент стал первым. Выведите массив \(a\)."""
def array32(a):
    l = len(a)
    for i in range(l):
        a[(i + 1) % l],a[i % l] = a[i % l],a[(i - 1) % l]
    print(a)


array32([1, 2, 3])
array32([4, 1, 2, 3])
array32([3, 4, 1, 2])


def array33():
    pass


array33()
array33()
array33()


def array34():
    pass


array34()
array34()
array34()


def array35():
    pass


array35()
array35()
array35()


def array36():
    pass


array36()
array36()
array36()


def array37():
    pass


array37()
array37()
array37()


def array38():
    pass


array38()
array38()
array38()


def array39():
    pass


array39()
array39()
array39()


def array40():
    pass


array40()
array40()
array40()


def array41():
    pass


array41()
array41()
array41()


def array42():
    pass


array42()
array42()
array42()


def array43():
    pass


array43()
array43()
array43()


def array44():
    pass


array44()
array44()
array44()


def array45():
    pass


array45()
array45()
array45()


def array46():
    pass


array46()
array46()
array46()


def array47():
    pass


array47()
array47()
array47()


def array48():
    pass


array48()
array48()
array48()


def array49():
    pass


array49()
array49()
array49()


def array50():
    pass


array50()
array50()
array50()
