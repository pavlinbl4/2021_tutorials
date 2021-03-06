# Задача_1
"""Дано число n. Выведите числа от 0 до n (не включая n)."""


# def req1(n, per=0):
#     if n > 0:
#         print(per)
#         req1(n - 1, per + 1)


def req1(n):
    if n > 0:
        req1(n - 1)
        print(n - 1)


# req1(0)
# req1(1)
# req1(5)


# Задача_2
"""Дано число n. Выведите числа от 1 до n (включая n)."""


def req2(n):
    if n > 0:
        req2(n - 1)
        print(n)


# req2(0)
# print("-" * 50)
# req2(1)
# print("-" * 50)
# req2(5)


# Задача_3
"""Дано число n. Выведите n раз число 1."""


def req3(n):
    if n > 0:
        print(1)
        req3(n - 1)


# req3(0)
# print("-" * 50)
# req3(1)
# print("-" * 50)
# req3(3)


# Задача_4
"""Дано число n. Выведите n раз число n."""


def req4(n, count=0):
    if count < n:
        print(n)
        req4(n, count + 1)


# req4(0)
# print("-" * 50)
# req4(1)
# print("-" * 50)
# req4(3)

# Задача_5
"""Дано число n и строка s. Выведите n раз строку s."""


def req5(n, s):
    if n > 0:
        print(s)
        req5(n - 1, s)


# req5(0, 'qwerty')
# print("-" * 50)
# req5(1, 'qwerty')
# print("-" * 50)
# req5(3, 'abc')


# Задача_6
"""Дано число n. Выведите числа от n (включительно) до 1 (включительно)."""


def req6(n):
    if n > 0:
        print(n)
        req6(n - 1)


# req6(0)
# print("-" * 50)
# req6(1)
# print("-" * 50)
# req6(3)


# Задача_7
"""Дано число n. Выведите числа от n (не включительно) до 0 (включительно)."""


def req7(n):
    if n > 0:
        print(n - 1)
        req7(n - 1)


# req7(0)
# print("-" * 50)
# req7(1)
# print("-" * 50)
# req7(3)


# Задача_8
"""Дано число n. Выведите числа от 1 (включительно) до n (включительно) с шагом 2."""


def req8(n, start=1):
    if n > 0:
        print(start)
        req8(n - 2, start + 2)


# req8(0)
# print("-" * 50)
# req8(1)
# print("-" * 50)
# req8(3)
# print("-" * 50)
# req8(6)


# Задача_9
"""Дано число n. Выведите числа от 2 (включительно) до n (включительно) с шагом 2."""


def req9(n, start=2):
    if n > 1:
        print(start)
        req9(n - 2, start + 2)


# req9(0)
# print("-" * 50)
# req9(1)
# print("-" * 50)
# req9(3)
# print("-" * 50)
# req9(6)


# Задача_10
"""Даны числа a и b (a <= b). Выведите числа от a (включительно) до b (включительно)."""


def req10(a, b):
    if b >= a:
        print(a)
        req10(a + 1, b)


# req10(0, 1)
# print("-" * 50)
# req10(5, 7)
# print("-" * 50)
# req10(10, 15)


# Задача_11
"""Даны числа a и b (a <= b). Выведите числа от b (не включительно) до a (не включительно)."""


def req11(a, b):
    if b - a > 1:
        print(b - 1)
        req11(a, b - 1)


# req11(0, 1)
# req11(5, 7)
# req11(10, 15)


# Задача_12
"""Дано вещественное число p - цена 1 кг конфет, а также целое число n. 
Выведите стоимость от 1 до n (включительно) кг конфет."""


def req12(p, n, count=1):
    if count <= n:
        print(count * p)
        req12(p, n, count + 1)


# req12(300, 3)
# req12(199.75, 4)


# Задача_13
"""Дано вещественное число p - цена 1 кг конфет, а также целое число n. 
Выведите стоимость 0.1 кг конфет, затем 0.2 кг, и т. д. до n * 0.1 кг конфет."""


def req13(p, n, count=1):
    if count <= n:
        print(count * p / 10)
        req13(p, n, count + 1)


# req13(300, 3)
# req13(199.75, 4)


# Задача_14
"""Дано вещественное число p - цена 1 кг конфет, а также целое число n. 
Выведите стоимость 1.2 кг конфет, затем 1.4 кг и т. д. с шагом 0.2. Всего n чисел."""


def req14(p, n, count=1):
    if n - count >= 0:
        print(round((1 + 2 * count / 10) * p, 2))
        req14(p, n, count + 1)


# req14(100, 3)
# req14(149.5, 4)


# Задача_15
"""Дано целое число n. 
Выведите числа от n (не включительно) до 0 (включительно) c шагом 2."""


def req15(n):
    if n > 0:
        print(n - 1)
        req15(n - 2)


# req15(1)
# req15(3)
# req15(4)


# Задача_16
"""Дано целое число n. Выведите числа от n (включительно) до 0 (не включительно) c шагом 2."""


def req16(n):
    if n > 0:
        print(n)
        req16(n - 2)


# req16(1)
# req16(3)
# req16(4)


# Задача_17
"""Дано целое число n. 
Выведите числа от 2 до n (включительно), которые делятся на 2 или на 3."""


def req17(n, count=2):
    if n - count >= 0:
        if count % 2 == 0 or count % 3 == 0:
            print(count)
        req17(n, count + 1)


# req17(3)
# req17(6)


# Задача_18
"""Дано целое число n. 
Выведите числа от 2 до n (включительно), 
которые делятся на 2 или на 3 в обратном порядке."""


def req18(n):
    if n >= 2:
        if n % 2 == 0 or n % 3 == 0:
            print(n)
        req18(n - 1)


# req18(5)
# req18(6)


# Задача_19
"""Дано целое число n. 
Выведите n чисел таких, что первое число - это 1, второе - 1+2, третье 1+2+3 и т. д.."""


def req19(n, s=0, count=1):
    if n - count >= 0:
        s += count
        print(s)
        req19(n, s, count + 1)


# req19(3)
# req19(5)


# Задача_20
"""Дано целое число n. 
Выведите n чисел таких, что первое число - это 1, второе - 1*2, третье 1*2*3 и т. д.."""


def req20(n, s=1, count=1):
    if n - count >= 0:
        s *= count
        print(s)
        req20(n, s, count + 1)


# req20(3)
# req20(5)


# Задача_21
"""Дано целое число n. Выведите n первых чисел, заканчивающихся на 4 или 7."""


def req21(n, count=1, a=3, x=4):
    if n - count >= 0:
        print(x)
        x += a
        a = 10 - a
        req21(n, count + 1, a, x)


# req21(1)
# req21(2)
# req21(4)


# Задача_22
"""Дано целое число n. 
Выведите n чисел, являющихся накопительной суммой чисел, заканчивающихся на 4 или 7. 
То есть, первое число 4, затем 4+7, 4+7+14 и т. д."""


def req22(n, count=1, x=4, a=3, answer=0):
    if n - count >= 0:
        answer += x
        x += a
        a = 10 - a
        print(answer)
        req22(n, count + 1, x, a, answer)


# req22(1)
# req22(2)
# req22(4)


# Задача_23
"""Дано целое число n. 
Выведите строки вида x * 2 = y, где x - это числа от 1 до n включительно, а y = x * 2."""


def req23(n, x=1):
    if n - x >= 0:
        print(f'{x} * 2 = {x * 2}')
        req23(n, x + 1)


# req23(2)
# req23(4)


# Задача_24 - аналогично 23 только m  вместо 2
"""Даны целые числа n и m. 
Выведите строки вида x * m = y, где x - это числа от 1 до n включительно, а y = x * m."""


def req24(n, m, x=1):
    if n - x >= 0:
        print(f'{x} * {m} = {x * m}')
        req24(n, m, x + 1)


# req24(2, 5)
# req24(4, 3)


# Задача_25
"""Дано целое число n. Выведите n чисел, чередуя 0 и 1."""


def req25(n, count=0):
    if n - count > 0:
        print(count % 2)
        req25(n, count + 1)


# req25(2)
# req25(5)


# Задача_26
"""Дано целое число n. Выведите n чисел, чередуя 0, 1 и 2."""


def req26(n, count=0):
    if n - count > 0:
        print(count % 3)
        req26(n, count + 1)


# req26(2)
# req26(5)


# Задача_27
"""Дано целое число n. Выведите n чисел, чередуя 1 и -1."""


def req27(n, count=1, x=1):
    if n - count >= 0:
        print(x)
        req27(n, count + 1, -x)


# req27(2)
# req27(5)


# Задача_28
"""Дано целое число n. Выведите n чисел, чередуя 1 и 2."""


def req28(n, count=1):
    if n - count >= 0:
        print(2 - count % 2)
        req28(n, count + 1)


# req28(2)
# req28(5)


# Задача_29
"""Дано целое число n. Выведите n чисел, чередуя 1, 2 и 3."""


def req29(n, count=0):
    if n - count > 0:
        print(count % 3 + 1)
        req29(n, count + 1)


# req29(2)
# req29(5)


# Задача_30
"""Дано целое число n. Выведите n чисел, чередуя 1 и 0"""


def req30(n, x=1):
    if n - x >= 0:
        print(x % 2)
        req30(n, x + 1)


# req30(2)
# req30(5)


# Задача_31
"""Дано целое число n. Выведите n чисел, чередуя 2, 1 и 0"""


def req31(n, count=0):
    if n - count > 0:
        print(2 - count % 3)
        req31(n, count + 1)


# req31(2)
# req31(5)


# Задача_32
"""Дано целое число n. Выведите n чисел, чередуя 1, 2 и 3, но каждое второе число отрицательное."""


def req32(n, count=0, x=1):
    if n - count > 0:
        print((count % 3 + 1) * x)
        req32(n, count + 1, -x)


# req32(2)
# req32(6)


# Задача_33
"""Дано целое число n. Выведите n чисел, чередуя 0, 2 и 4."""


def req33(n, count=0):
    if n - count > 0:
        print(count % 3 * 2)
        req33(n, count + 1)


# req33(2)
# req33(5)


# Задача_34
"""Дано целое число n. Выведите n чисел, чередуя 2, 4 и 6."""


def req34(n, count=0):
    if n - count > 0:
        print((count % 3 + 1) * 2)
        req34(n, count + 1)


# req34(2)
# req34(5)


# Задача_35
"""Дано целое число n. Выведите все пары положительных чисел, которые в сумме дают n.
Сначала меньшее число, затем большее."""


def req35(n, count=1):
    if count * 2 <= n:
        print(count, n - count)
        req35(n, count + 1)


# req35(8)
# req35(7)


# Задача_36
"""Дано целое число n. 
Выведите первые n букв латинского алфавита в нижнем регистре (строчные)."""


def req36(n, count=0):
    if n - count > 0:
        print(chr(ord("a") + count))
        req36(n, count + 1)


# req36(1)
# req36(3)


# Задача_37
"""Дано целое число n. 
Выведите последние n букв латинского алфавита в верхнем регистре (заглавные)."""


def req37(n, count=1):
    if n - count >= 0:
        print(chr(ord("Z") - n + count))
        req37(n, count + 1)


# req37(1)
# req37(3)


# Задача_38
"""
Дан символ c - строчная латинская буква.
Выведите буквы алфавита до c (включительно) с шагом 2."""


def req38(c, count=0):
    if ord(c) - count >= ord('a'):
        print(chr(ord('a') + count))
        req38(c, count + 2)


# req38('f')
# req38('d')


# Задача_39
"""Даны символы a и b - строчные латинские буквы. 
Выведите пары букв из последовательности от a до b: 
первая и последняя, затем вторая и предпоследняя, и т. д., пока не встретятся в центре."""


def req39(a, b):
    if b > a:
        print(a, b)
        req39(chr(ord(a) + 1), chr(ord(b) - 1))


# req39('a', 'c')
# req39('b', 'e')


# Задача_40
"""Дано целое число n. 
Вывести первые n пар букв, соседних в алфавите, в верхнем регистре, начиная от AB. (AB, BC, CD...)."""


def req40(n, count=0):
    if n - count > 0:
        print(chr(65 + count), chr(66 + count), sep="")
        req40(n, count + 1)


# req40(1)
# req40(3)
