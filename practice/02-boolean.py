def boolean1(a):
    print(a > 0)


# boolean1(5)
# boolean1(0)
# boolean1(-4)


def boolean2(a):
    print(a % 2 == 0)


# boolean2(5)
# boolean2(0)
# boolean2(6)


def boolean3(a):
    print(a % 2 != 0)


# boolean3(5)
# boolean3(0)
# boolean3(6)


def boolean4(a):
    print(a % 10 == 4 or a % 10 == 7)


# boolean4(14)
# boolean4(57)
# boolean4(42)


def boolean5(a):
    print(a % 10 != 4 and a % 2 == 0)


# boolean5(14)
# boolean5(57)
# boolean5(42)


def boolean6(a, b):
    print(a > 0 and b > 0)


# boolean6(5, 6)
# boolean6(0, 3)
# boolean6(-1, -2)


def boolean7(a, b):
    print(a > 0 or b > 0)


# boolean7(5, 6)
# boolean7(0, 3)
# boolean7(-1, -2)


def boolean8(a, b):
    # print(a >= 0 and b < 0 or a < 0 and b >= 0)
    print(a * b < 0)


# boolean8(5, -6)
# boolean8(-5, 6)
# boolean8(5, 6)
# boolean8(-5, -6)
# boolean8(5, 0)


def boolean9(a, b, c):
    print(a < b < c)


# boolean9(5, 10, 11)
# boolean9(5, 11, 10)
# boolean9(7, 7, 7)


def boolean10(a, b, c):
    print(a < b < c or c < b < a)



# boolean10(5, 10, 11)
# boolean10(11, 10, 5)
# boolean10(11, 10, 10)


def  boolean11(a):
    print(9 < a < 100)


# boolean11(50)
# boolean11(9)
# boolean11(100)


def boolean12(a):
    print(a % 2 != 0 and 99 < a < 1000  or 9 < a < 100 and a % 2 == 0)

# boolean12(8)
# boolean12(9)
# boolean12(51)
# boolean12(52)
# boolean12(100)
# boolean12(101)
# boolean12(9998)
# boolean12(9999)


def boolean13(a):
    a4 = a % 10
    a3 = a // 10 % 10
    a2 = a // 100 % 10
    a1 = a // 1000
    print(a1 == a4 and a2 == a3)

# boolean13(1001)
# boolean13(9999)
# boolean13(1233)


def boolean14(n):
    print(n % 4 == 0 and n % 100 != 0 or n % 100 == 0 and n % 400 == 0)


# boolean14(2020)
# boolean14(1996)
# boolean14(1990)
# boolean14(2000)
# boolean14(1900)


def boolean15(a,b,c):
    print(a + b > c and a + c > b and c + b > a)


# boolean15(1, 1, 1)
# boolean15(3, 4, 5)
# boolean15(1, 2, 3)
# boolean15(7, 3, 3)


