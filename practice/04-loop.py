def loop1(n):
    for i in range(n):
        print(i)


# loop1(0)
# loop1(1)
# loop1(3)


def loop2(n):
    for i in range(1, n + 1):
        print(i)


# loop2(0)
# loop2(1)
# loop2(3)


def loop3(n):
    for i in range(n):
        print(1)


# loop3(0)
# loop3(1)
# loop3(3)


def loop4(n):
    for i in range(n):
        print(n)


# loop4(0)   # как пакетно переименовать loop3 в loop4 если они записаны столбиком ?
# loop4(1)
# loop4(3)


def loop5(n, s):
    for i in range(n):
        print(s)


# loop5(0, 'qwerty')
# loop5(1, 'qwerty')
# loop5(3, 'abc')


def loop6(n):
    for i in range(n, 0, -1):
        print(i)


# loop6(0)
# loop6(1)
# loop6(3)


def loop7(n):
    for i in range(n - 1, - 1, -1):
        print(i)


# loop7(0)
# loop7(1)
# loop7(3)


def loop8(n):
    for i in range(1, n + 1, 2):
        print(i)


# loop8(0)
# loop8(1)
# loop8(3)
# loop8(6)


def loop9(n):
    for i in range(2, n + 1, 2):
        print(i)


# loop9(0)
# loop9(1)
# loop9(3)
# loop9(6)


def loop10(a, b):
    for i in range(a, b + 1):
        print(i)


# loop10(0, 1)
# loop10(5, 7)
# loop10(10, 10)  # 23 минуты в полусонном состоянии на 10 задач


def loop11(a, b):
    for i in range(b - 1, a, -1):
        print(i)


# loop11(0, 1)
# loop11(5, 7)
# loop11(10, 15)


def loop12(p, n):
    for i in range(1, n + 1):
        print(i * p)


# loop12(300, 3)
# loop12(199.75, 4)


def loop13(p, n):  # нужно ли здесь округлять результат ?
    for i in range(1, n + 1):
        print(i * p / 10)


# loop13(300, 3)
# loop13(199.75, 4)


def loop14(p, n):  # неожиданно сложная задача
    for i in range(12, 12 + n * 2, 2):
        print(i * p / 10)


# loop14(100, 3)
# loop14(149.5, 4)


def loop15(n):  # не с 1 раза :-(
    for i in range(n - 1, -1, -2):
        print(i)


# loop15(1)
# loop15(3)
# loop15(4)


def loop16(n):
    for i in range(n, 0, -2):
        print(i)


#
# loop16(1)
# loop16(3)
# loop16(4)


def loop17(n):
    for i in range(2, n + 1):
        if i % 2 == 0 or i % 3 == 0:
            print(i)


# loop17(3)
# loop17(6)


def loop18(n):
    for i in range(n, 1, -1):
        if i % 2 == 0 or i % 3 == 0:
            print(i)


# loop18(5)
# loop18(6)


def loop19(n):
    x = 0
    for i in range(1, n + 1):
        x += i
        print(x)


# loop19(3)
# loop19(5)


def loop20(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
        print(x)


# loop20(3)
# loop20(5)

"""Дано целое число n. Выведите n первых чисел, заканчивающихся на 4 или 7."""
def loop21(n):
    # count = 0
    # i = 0
    # while count < n:
    #     i += 1
    #     if i % 10 == 4 or i % 10 == 7:
    #         print(i)
    #         count += 1

    # for i in range(4, n * 5):
    #     if i % 10 == 4 or i % 10 == 7:
    #         print(i)

    # x = 4
    # for i in range(n):
    #     print(x)
    #     x += 3 if i % 2 == 0 else 7

    # x = 4
    # for i in range(n):
    #     print(x)
    #     x += i % 2 * 4 + 3

    x = 4
    a = 3
    for i in range(n):
        print(x)
        x += a
        a = 10 - a


# loop21(1)
# loop21(2) 
# loop21(4)


def loop22(n):
    # count = 0
    # i = 0
    # summ = 0
    # while count < n:
    #     i += 1
    #     if i % 10 == 4 or i % 10 == 7:
    #         summ += i
    #         count += 1
    #         print(summ)

    x = 4
    a = 3
    s = 0
    for i in range(n):
        s += x
        print(s)
        x += a
        a = 10 - a


# loop22(1)
# loop22(2)
# loop22(4)


def loop23(n):
    for x in range(1, n + 1):
        print(f'{x} * 2 = {x * 2}')


# loop23(2)
# loop23(4)


def loop24(n, m):
    for x in range(1, n + 1):
        print(f'{x} * {m} = {x * m}')


# loop24(2, 5)
# loop24(4, 3)


def loop25(n):
    # for i in range(1, n + 1):
    #     # print(0 if i % 2 == 0 else 1)
    #     print(1 - i % 2)
    for i in range(n):
        print(i % 2)


# loop25(2)
# loop25(5)


def loop26(n):
    for i in range(n):
        print(i % 3)


# loop26(2)
# loop26(5)


def loop27(n):
    # for i in range(1, n + 1):
    #     # print(-1 if i % 2 == 0 else 1)
    #     print( - 2 * (i % 2) + 1)

    # for i in range(n):
    #     print(1 - i % 2 * 2)

    x = 1
    for i in range(n):
        print(x)
        x = -x


# loop27(2)
# loop27(5)


def loop28(n):
    for i in range(n):
        print(i % 2 + 1)


# loop28(2)
# loop28(5)

def loop29(n):
    for i in range(n):
        print(i % 3 + 1)


# loop29(2)
# loop29(5)


def loop30(n):
    for i in range(1, n + 1):
        print(i % 2)


# loop30(2)
# loop30(5)


# x - 0 = 2
# x - 1 = 1
# x - 2 = 0
def loop31(n):
    for i in range(n):
        print(2 - i % 3)


# loop31(2)
# loop31(5)
# loop31(6)


def loop32(n):
    znak = 1
    for i in range(n):
        print((i % 3 + 1) * znak)
        znak *= -1


# loop32(2)
# loop32(6)


def loop33(n):
    for i in range(n):
        print(i % 3 * 2)


# loop33(2)
# loop33(5)


def loop34(n):
    for i in range(n):
        print(i % 3 * 2 + 2)


# loop34(2)
# loop34(5)


def loop35(n):
    for i in range(1, n // 2 + 1):
        print(i, n - i)


# loop35(8)
# loop35(7)


def loop36(n):
    for x in range(97, 97 + n):
        print(chr(x))


# loop36(1)
# loop36(3)


def loop37(n):
    # for i in range(n):
    for x in range(ord('Z') - n + 1, ord('Z') + 1):
        print(chr(x))


# loop37(1)
# loop37(3)


def loop38(n):
    for x in range(97, ord(n) + 1, 2):
        print(chr(x))


# loop38('f')
# loop38('c')


def loop39(a, b):
    # st1 = ord(a)
    # st2 = ord(b)
    # for i in range(st1, st2 - (st2 - st1) // 2):
    #     print(chr(i), chr(st2 - (i - st1)))
    x = ord(a)
    y = ord(b)
    while x < y:
        print(chr(x), chr(y))
        x += 1
        y -= 1


# loop39('a', 'c')
# loop39('b', 'e')

def loop40(n):
    for x in range(65, 65 + n):
        print(chr(x) + chr(x + 1))

# loop40(1)
# loop40(3)
