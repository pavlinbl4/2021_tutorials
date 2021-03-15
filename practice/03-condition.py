def condition1(a):
    # if a > 0:
    #     a += 1
    # print(a)

    # a = a + 1 if a > 0 else a
    a += a > 0
    print(a)


# condition1(5)
# condition1(0)
# condition1(-1)


def condition2(a):
    print(a + 1 if a > 0 else a - 2)


# condition2(5)
# condition2(0)
# condition2(-1)


def condition3(a):  # долго не получался синтаксис -  тернарный оператор
    # print(a + 1 if a > 0 else a - 2 if a == 0 else 10)
    print(a + 1 if a > 0 else a - 2 if a < 0 else 10)


# condition3(5)
# condition3(0)
# condition3(-1)


def condition4(a, b):  # нужнои и можно ли использовать тернарный оператор ?
    if a % 2 == 0:
        a += b
    else:
        b -= a
    print(a, b)


# condition4(4, 6)
# condition4(5, 6)
# condition4(7, 4)


def condition5(a, b, c):
    if a % 2 == 0:
        b += 1
        c += 1
    if b % 2 == 0 and c % 2 != 0:
        a -= 2
    print(a, b, c)


# condition5(4, 5, 6)
# condition5(4, 3, 5)
# condition5(7, 6, 5)


def condition6(a, b, c):
    s = 0
    if a % 2 == 0:
        s += a
    if b % 2 == 0:
        s += b
    if c % 2 == 0:
        s += c
    print(s)


# condition6(4, 7, 8)
# condition6(3, 5, 6)
# condition6(3, 5, 7)


def condition7(a, b, c):
    # maxd = None
    # if a > b and a > c:
    #     maxd = a
    # elif b > c:
    #     maxd = b
    # else:
    #     maxd = c
    # print(maxd)

    # if a < b:
    #     a, b = b, a
    # if a < c:
    #     a, c = c, a

    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    print(m)


# condition7(5, 8, 2)
# condition7(3, 5, 6)
# condition7(7, 7, 2)


def condition8(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    print(a, b, c)


# condition8(5, 8, 2)
# condition8(3, 5, 6)
# condition8(-1, -2, -3)


def condition9(a, b, c):
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a
    print(a, b, c)


# condition9(5, 8, 2)
# condition9(3, 5, 6)
# condition9(-1, -2, -3)


def condition10(a, b, c):
    # if a >= b and a >= c:
    #     print(1)
    # elif b >= c and b >= a:
    #     print(2)
    # elif c >= a and c >= b:
    #     print(3)
    m = a
    numb = 1
    if b > m:
        m = b
        numb = 2
    if c > m:
        numb = 3
    print(numb)


# condition10(5, 8, 2)
# condition10(3, 5, 6)
# condition10(7, 7, 2)


def condition11(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    print(c - a)


# condition11(5, 8, 2)
# condition11(3, 5, 6)
# condition11(20, 5, 10)


def condition13(a, b, c):
    # if (a + b + c) % 2 != 0:
    #     a *= 2
    #     b *= 2
    #     c *= 2
    # else:
    #     a *= -1
    #     b *= -1
    #     c *= -1
    q = 2 if (a + b + c) % 2 != 0 else -1
    a *= q
    b *= q
    c *= q
    print(a, b, c)


# condition13(1, 2, 3)
# condition13(2, 3, 4)
# condition13(3, 3, 3)


def condition14(a, b, c):
    # if a % 10 == 4 or b % 10 == 4 or c % 10 == 4:
    #     if a > b:
    #         a, b = b, a
    #     if b > c:
    #         c, b = b, c
    #     print(c)
    # else:
    #     m = a
    #     if a > b:
    #         m = b
    #     if c < m:
    #         m = c
    #     print(m)
    m = a
    if a % 10 == 4 and b % 10 == 4 and c % 10 == 4:
        if b > m:
            m = b
        if c > m:
            m = c
    else:
        if b < m:
            m = b
        if c < m:
            m = c
    print(m)


condition14(3, 4, 5)
condition14(5, 6, 7)
condition14(4, 24, 14)
condition14(7, 5, 3)


def condition15(a, b, c):
    if a + b == c:
        print(f'{a} + {b} = {c}')
    elif a - b == c:
        print(f'{a} - {b} = {c}')
    else:
        print(f'{a} + {b} = {a + b}, {a} - {b} = {a - b}')


# condition15(10, 20, 30)
# condition15(30, 20, 10)
# condition15(3, 4, 5)


def condition16(a, b):
    print("Вася" if a > b else "Петя" if b > a else "ничья")


# condition16(20, 15)
# condition16(15, 20)
# condition16(10, 10)


def condition17(a, b):
    # print(abs(a - b) if a != b else 0)
    # print(abs(a - b))
    print(a - b if a > b else b - a)


# condition17(20, 15)
# condition17(20, 25)
# condition17(10, 10)


def condition18(a, b):
    print("YES" if a - b >= 2 or b - a >= 2 else "NO")


# condition18(20, 15)
# condition18(20, 15)
# condition18(10, 11)
# condition18(10, 10)


def condition19(v, p):
    if v == p:
        print("ничья")
    # elif v == "k" and p == "n" or v == "n" and p == "b" or v == "b" and p == "k":
    elif v + p in ("kn", "nb", "bk"):
        print("Вася")
    else:
        print("Петя")


# condition19('k', 'n')
# condition19('b', 'n')
# condition19('b', 'k')
# condition19('n', 'n')


def condition20(r, m, s):
    # if m + s > r and r >= m and r >= s:
    #     print("мороженое")
    # elif m + s > r and r < m and r >= s:
    #     print("шоколад")
    # elif r < m and r < s:
    #     print("ничего")
    # elif m + s <= r:
    #     print("и то, и другое")
    if r >= m + s:
        print('и то, и другое')
    elif r >= m:
        print('мороженое')
    elif r >= s:
        print("шоколад")
    else:
        print("ничего")


# condition20(100, 30, 40)
# condition20(100, 50, 100)
# condition20(100, 120, 100)
# condition20(100, 120, 120)
