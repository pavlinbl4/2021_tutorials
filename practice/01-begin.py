def begin1(a):
    print(4 * a)


# begin1(1)
# begin1(12)


def begin2(a):
    print(a ** 2)


# begin2(1)
# begin2(12)


def begin3(a, b):
    print(a * b, 2 * (a + b))


# begin3(5, 4)
# begin3(10, 10)


def begin4(a):
    print(a ** 3, 6 * a ** 2)


# begin4(5)
# begin4(10)

def begin5(a, b):  # home work
    print((a + b) / 2)


# begin5(5, 7)
# begin5(2, -3)


def begin6(a, b):
    print((a * b) ** 0.5)


# begin6(2, 8)
# begin6(0, 5)
# begin6(7, 9)


def begin7(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    print(c, a + b + c)


# begin7(3, 4)
# begin7(5, 7)


def begin8(a, b):
    print(abs(a - b))


# begin8(1, 4)
# begin8(1, -4)


def begin9(a, b):
    c = b
    b = a
    a = c
    # a, b = b, a
    print(a, b)


# begin9(1, 4)
# begin9(10, 15)


def begin10(a, b, c):
    a, b, c = b, c, a
    print(a, b, c)


# begin10(1, 4, 7)
# begin10(10, 15, 20)


def begin11(a):
    a *= a
    print(a)
    a *= a
    print(a)
    a *= a
    print(a)


# begin11(1)
# begin11(2)
# begin11(10)


def begin12(w1, p1, w2):
    print(p1 / w1, p1 / w1 * w2)


# begin12(3, 300, 2)
# begin12(1.5, 450, 0.5)


def begin13(r):
    print(r % 10)


# begin13(5)
# begin13(27)
# begin13(150)
# begin13(199)


def begin14(m):
    print(m % 60)


# begin14(5)
# begin14(59)
# begin14(70)
# begin14(180)


def begin15(d):
    print(d % 7)


# begin15(0)
# begin15(6)
# begin15(7)
# begin15(29)


def begin16(d):  # home work  !!!!!!
    print((d + 1) % 7)


# begin16(0)
# begin16(3)
# begin16(6)  # если 6 дней назад был вторник, то сегодня понедельник ?
# begin16(29)


def begin17(d):  # home work (как то туго пошло)
    print(d % 7)


# begin17(0)
# begin17(3)
# begin17(7)
# begin17(29)


def begin18(d):  # home work
    print(d % 7 + 1)


# begin18(0)
# begin18(6)
# begin18(7)
# begin18(29)


def begin19(a):
    print(a // 10, a % 10)


# begin19(10)
# begin19(91)


def begin20(a):  # home work
    b = a % 10
    c = a // 10
    print(b + c, b * c)


# begin20(27)
# begin20(55)


def begin21(a):
    print(a % 2)


# begin21(0)
# begin21(1)
# begin21(5)
# begin21(10)


def begin22(a):  # home work
    print(a % 2 + 1)


# begin22(0)
# begin22(1)
# begin22(5)
# begin22(10)


# x - 0 = 1
# x - 1 = 0
def begin23(a):  # home work
    print(1 - a % 2)


# begin23(0)
# begin23(1)
# begin23(5)
# begin23(10)


def begin24(a):  # home work
    print(2 - a % 2)


# begin24(0)
# begin24(1)
# begin24(5)
# begin24(10)


def begin25(n):
    print((n - 1) % 3)

# begin25(1)
# begin25(3)
# begin25(5)
# begin25(10)
