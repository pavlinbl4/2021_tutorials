def akerr(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return akerr(m - 1, 1)
    if m > 0 and n > 0:
        return akerr(m-1, akerr(m, n - 1))


print(akerr(3, 2))
