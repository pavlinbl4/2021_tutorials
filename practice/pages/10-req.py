# Задача_1
"""
Дано число n. Выведите числа от 0 до n (не включая n).
"""


def req1(n):
    if n == 0:
        return 0
    return req1(n - 1)




req1(0)   #
req1(1)   # 0
print(req1(3))  # 0
1
2



# Задача_2
"""Дано число n. Выведите числа от 1 до n (включая n)."""


def req2():
    pass



req2(0)   #
req2(1)   # 1
req2(3)   # 1
2
3



# Задача_3
"""Дано число n. Выведите n раз число 1."""


def req3():
    pass



req3(0)   #
req3(1)   # 1
req3(3)   # 1
1
1



# Задача_4
"""Дано число n. Выведите n раз число n."""


def req4():
    pass



req4(0)   #
req4(1)   # 1
req4(3)   # 3
3
3



# Задача_5
"""Дано число n и строка s. Выведите n раз строку s."""


def req5():
    pass



req5(0, 'qwerty')   #
req5(1, 'qwerty')   # qwerty
req5(3, 'abc')   # abc
abc
abc



# Задача_6
"""Дано число n. Выведите числа от n (включительно) до 1 (включительно)."""


def req6():
    pass



req6(0)   #
req6(1)   # 1
req6(3)   # 3
2
1



# Задача_7
"""Дано число n. Выведите числа от n (не включительно) до 0 (включительно)."""


def req7():
    pass



req7(0)   #
req7(1)   # 0
req7(3)   # 2
1
0



# Задача_8
"""Дано число n. Выведите числа от 1 (включительно) до n (включительно) с шагом 2."""


def req8():
    pass



req8(0)   #
req8(1)   # 1
req8(3)   # 1
3



# Задача_9
"""Дано число n. Выведите числа от 2 (включительно) до n (включительно) с шагом 2."""


def req9():
    pass



req9(6)   # 1
3
5
req9(0)   #
req9(1)   #



# Задача_10
"""Даны числа a и b (a \le b). Выведите числа от a (включительно) до b (включительно)."""


def req10():
    pass



req10(3)   # 2
req10(6)   # 2
4
6
req10(0, 1)   # 0
1



# Задача_11
"""Даны числа a и b (a \le b). Выведите числа от b (не включительно) до a (не включительно)."""


def req11():
    pass



req11(5, 7)   # 5
6
7
req11(10, 10)   # 10
req11(0, 1)   #



# Задача_12
"""Дано вещественное число p - цена 1 кг конфет, а также целое число n. Выведите стоимость от 1 до n (включительно) кг конфет."""


def req12():
    pass



req12(5, 7)   # 6
req12(10, 15)   # 14
13
12
11
req12(300, 3)   # 300
600
900



# Задача_13
"""Дано вещественное число p - цена 1 кг конфет, а также целое число n. Выведите стоимость 0.1 кг конфет, затем 0.2 кг, и т. д. до n * 0.1 кг конфет."""


def req13():
    pass



req13(199.75, 4)   # 199.75
399.5
599.25
799
req13(100, 3)   # 120
140
160
req13(149.5, 4)   # 179.4‬
209.3
239.2
269.1



# Задача_14
"""Дано вещественное число p - цена 1 кг конфет, а также целое число n. Выведите стоимость 1.2 кг конфет, затем 1.4 кг и т. д. с шагом 0.2. Всего n чисел."""


def req14():
    pass



req14(1)   # 0
req14(3)   # 2
0
req14(4)   # 3
1



# Задача_15
"""Дано целое число n. Выведите числа от n (не включительно) до 0 (включительно) c шагом 2."""


def req15():
    pass



req15(1)   # 1
req15(3)   # 3
1
req15(4)   # 4
2



# Задача_16
"""Дано целое число n. Выведите числа от n (включительно) до 0 (не включительно) c шагом 2."""


def req16():
    pass



req16(3)   # 2
3
req16(6)   # 2
3
4
6
req16(5)   # 4
3
2



# Задача_17
"""Дано целое число n. Выведите числа от 2 до n (включительно), которые делятся на 2 или на 3."""


def req17():
    pass



req17(6)   # 6
4
3
2
req17(3)   # 1
3
6
req17(5)   # 1
3
6
10
15



# Задача_18
"""Дано целое число n. Выведите числа от 2 до n (включительно), которые делятся на 2 или на 3 в обратном порядке."""


def req18():
    pass



req18(3)   # 1
2
6
req18(5)   # 1
2
6
24
120
req18(1)   # 4



# Задача_19
"""Дано целое число n. Выведите n чисел таких, что первое число - это 1, второе - 1+2, третье 1+2+3 и т. д.."""


def req19():
    pass



req19(2)   # 4
7
req19(4)   # 4
7
14
17
req19(1)   # 4



# Задача_20
"""Дано целое число n. Выведите n чисел таких, что первое число - это 1, второе - 1*2, третье 1*2*3 и т. д.."""


def req20():
    pass



req20(2)   # 4
11
req20(4)   # 4
11
25
42
req20(2)   # 0
1



# Задача_21
"""Дано целое число n. Выведите n первых чисел, заканчивающихся на 4 или 7."""


def req21():
    pass



req21(5)   # 0
1
0
1
0
req21(2)   # 0
1
req21(5)   # 0
1
2
0
1



# Задача_22
"""Дано целое число n. Выведите n чисел, являющихся накопительной суммой чисел, заканчивающихся на 4 или 7. То есть, первое число 4, затем 4+7, 4+7+14 и т. д."""


def req22():
    pass



req22(2)   # 1
-1
req22(5)   # 1
-1
1
-1
1
req22(2)   # 1
2



# Задача_23
"""Дано целое число n. Выведите строки вида x * 2 = y, где x - это числа от 1 до n включительно, а y = x * 2."""


def req23():
    pass



req23(5)   # 1
2
1
2
1
req23(2)   # 1
2
req23(5)   # 1
2
3
1
2



# Задача_24
"""Даны целые числа n и m. Выведите строки вида x * m = y, где x - это числа от 1 до n включительно, а y = x * m."""


def req24():
    pass



req24(2)   # 1
0
req24(5)   # 1
0
1
0
1
req24(2)   # 2
1



# Задача_25
"""Дано целое число n. Выведите n чисел, чередуя 0 и 1."""


def req25():
    pass



req25(5)   # 2
1
0
2
1
req25(2)   # 1
-2
req25(6)   # 1
-2
3
-1
2
-3



# Задача_26
"""Дано целое число n. Выведите n чисел, чередуя 0, 1 и 2."""


def req26():
    pass



req26(2)   # 0
2
req26(5)   # 0
2
4
0
2
req26(2)   # 2
4



# Задача_27
"""Дано целое число n. Выведите n чисел, чередуя 1 и -1."""


def req27():
    pass



req27(5)   # 2
4
6
2
4
req27(8)   # 1 7
2 6
3 5
4 4
req27(7)   # 1 6
2 5
3 4



# Задача_28
"""Дано целое число n. Выведите n чисел, чередуя 1 и 2."""


def req28():
    pass



req28(1)   # a
req28(3)   # a
b
c
req28(1)   # Z



# Задача_29
"""Дано целое число n. Выведите n чисел, чередуя 1, 2 и 3."""


def req29():
    pass



req29(3)   # X
Y
Z
req29('f')   # a
c
e
req29('c')   # a
c



# Задача_30
"""Дано целое число n. Выведите n чисел, чередуя 1 и 0"""


def req30():
    pass



req30('a', 'c')   # a c
req30('b', 'e')   # b e
c d
req30(1)   # AB



