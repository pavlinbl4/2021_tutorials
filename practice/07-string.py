"""Дана строка s.
Выведите первый и последний символ из этой строки."""


def string1(s):
    print(s[0], s[-1])


# string1('qwerty')  # q y
# string1('test')  # t t
# string1('a')  # a a

'''Дана строка s. 
Выведите true, если она начинается с подстроки 'Hello' (без кавычек), иначе false.'''


def string2(s):
    print(s.startswith('Hello'))


# string2('Hello, world!')  # true
# string2('Test Hello')  # false
# string2('Helo')  # false

'''Дана строка s. 
Выведите true, если она заканчивается на подстроку 'end.' (без кавычек), иначе false.'''


def string3(s):
    # print("end." in s[-4:])
    print(s.endswith("end."))


# string3('End of string.')  # false
# string3('This is the end.')  # true
# string3('This is the end')  # false

'''Дана строка s. 
Выведите true, если она содержит подстроку 'middle', иначе false.'''


def string4(s):
    print("middle" in s)


# string4('Middle.')  # false
# string4('middle is here')  # true
# string4('String has a middle.')  # true

'''Дана строка s, содержащая пробелы в начале и в конце. 
Выведите эту строку без начальных и конечных пробелов.'''


def string5(s):
    print(s.strip())


# string5(' test ')  # test
# string5('  a   b')  # a   b
# string5('word1   word2   ')  # word1   word2

'''Дана строка s. 
Выведите эту строку в верхнем регистре (все буквы заглавные).'''


def string6(s):
    print(s.upper())


# string6('test')  # TEST
# string6('StRinG')  # STRING
# string6('1234, abc')  # 1234, ABC

'''Дана строка s. 
Выведите эту строку в нижнем регистре (все буквы строчные).'''


def string7(s):
    print(s.lower())


# string7('test')  # test
# string7('StRinG')  # string
# string7('1234, Abc')  # 1234, abc

'''Дана строка s, содержащая подстроку 'sub'. 
Выведите индекс первого вхождения подстроки 'sub'.'''


def string8(s):
    # print(s.index("sub"))
    print(s.find("sub"))


# string8('sub')  # 0
# string8('test sub')  # 5
# string8('susubsub')  # 2


'''Дана строка s, содержащая подстроку 'sub'. 
Выведите индекс последнего вхождения подстроки 'sub'.'''


def string9(s):
    print(s.rfind("sub"))


# string9('sub')  # 0
# string9('test sub')  # 5
# string9('susubsub')  # 5

'''Дана строка s и число n. 
Выведите строку, содержащую исходную строку n раз.'''


def string10(s, n):
    print(s * n)


# string10('a', 3)  # aaa
# string10('123', 2)  # 123123
# string10('qwerty', 0)  #

'''Дана строка s. 
Выведите только вторую половину строки (вместе с центральным символом, если длина нечётная).'''


def string11(s):
    print(s[len(s) // 2:])


# string11('abc')  # bc
# string11('abcd')  # cd
# string11('qwert')  # ert

'''Дана строка s. 
Выведите только первую половину строки (без центрального символа, если длина нечётная).'''


def string12(s):
    print(s[:len(s) // 2])


# string12('abc')  # a
# string12('abcdefg')  # abc
# string12('1')  #

'''Дан символ c и строка s. 
Выведите строку с удвоенным первым вхождением символа c в строку s.'''


def string13(c, s):

    # inx = s.find(c)
    #
    # if inx >= 0:
    #     print(f"{s[:inx]}{c}{s[inx:]}")
    #     return
    print(s.replace(c, c * 2, 1))


# string13('b', 'abcabc')  # abbcabc
# string13('t', 'test')  # ttest
# string13('q', '1234')  # 1234

'''Дан символ c и строки s, s0. 
Перед первым вхождением символа c в строку s вставить строку s0.'''


def string14(c, s, s0):
    inx = s.find(c)
    if inx >= 0:
        # print(f"{s[:inx]}{s0}{s[inx:]}")
        print(s[:inx] + s0 + s[inx:])
        return
    print(s)


# string14('b', 'abcabc', '#')  # a#bcabc
# string14('t', 'test', '$$')  # $$test
# string14('q', '1234', 'abc')  # 1234

'''Дан символ c и строки s, s0. 
После первого вхождения символа c в строку s вставить строку s0.'''


def string15(c, s, s0):
    # inx = s.find(c)
    # if inx >= 0:
    #     print(s[:(inx + 1)] + s0 + s[(inx + 1):])
    #     return
    # print(s)
    inx = s.find(c) + 1
    if inx >= 0:
        print(s[:inx] + s0 + s[inx:])
        return
    print(s)


# string15('b', 'abcabc', '#')  # ab#cabc
# string15('t', 'test', '$$')  # t$$est
# string15('q', '1234', 'abc')  # 1234

'''Даны строки s и s0. 
Проверить, содержится ли строка s0 в строке s. 
Если содержится, то вывести true, если не содержится, то вывести false.'''


def string16(s, s0):
    print(s0 in s)


# string16('abcabc', 'bc')  # true
# string16('test', 'test')  # true
# string16('1234', 'abc')  # false

'''Даны строки s и s0. 
Удалить из строки s первое вхождение s0.'''


def string17(s, s0):
    inx = s.find(s0)
    if inx >= 0:
        print(s[:inx] + s[(inx + len(s0)):])
        return
    print(s)


# string17('abcabc', 'bc')  # aabc
# string17('test', 'test')  #
# string17('1234', 'abc')  # 1234

'''Даны строки s, s0 и s1. 
Заменить в строке s первое вхождение строки s0 на строку s1.'''


def string18(s, s0, s1):
    inx = s.find(s0)
    if inx >= 0:
        print(s[:inx] + s1 + s[(inx + len(s0)):])
        return
    print(s)


# string18('abcabc', 'bc', 'BC')  # aBCabc
# string18('test', 'test', 'xyz')  # xyz
# string18('1234', 'abc', 'qwe')  # 1234

'''Дана строка s, и числа m и n (0 <= m <= n < |s|). 
Выведите подстроку, содержащую символы строки s начиная с индекса m (включительно) до  индекса n (не включительно).'''


def string19(s, m, n):
    print(s[m:n])


# string19('abcabc', 2, 5)  # cab
# string19('test', 0, 4)  # test
# string19('1234', 2, 2)  #

'''Дана строка s, содержащая один или более пробелов. 
Вывести подстроку, расположенную между первым и последним пробелом. 
Если s содержит только один пробел, то вывести пустую строку.'''


def string20(s):
    s1 = s.find(" ") + 1
    s2 = s.rfind(" ")
    print(s[s1:s2])


# string20('abc abc')  #
# string20('test abc qwe xyz')  # abc qwe
# string20('1234   5 678')  # 5

'''Даны строка s и целое число n. 
Выведите строку длины n: если длина s больше n, то вывести последние n символов из s, 
а если меньше, то заполнить недостающие символы точками ('.') в начале.'''


def string21(s, n):
    if len(s) > n:
        print(s[-n:])
    else:
        # print("." * (n - len(s)) + s)
        print(s.rjust(n, '.'))


# string21('abc xyzxyz', 3)  # xyz
# string21('abc', 7)  # ....abc
# string21('1234', 4)  # 1234

'''Даны числа n1 и n2 и строки s1 и s2. 
Получить из этих строк новую строку, содержащую первые n1 символов строки s1 и последние n2 символов строки s2.'''


def string22(n1, n2, s1, s2):
    print(s1[:n1] + s2[-n2:])


# string22(3, 5, 'aaabbb', 'cccddd')  # aaaccddd
# string22(1, 1, '123', '456')  # 16
# string22(8, 5, 'I love cats', 'coding')  # I love coding

'''Дана строка s, состоящая из слов, разделённых одиночными пробелами. 
Выведите количество слов, которые начинаются с заглавной буквы.'''


def string23(s):
    # count = 0
    # words = s.split()
    # for i in words:
    #     if i[0].isupper():
    #         count += 1
    # print(count)
    print(sum(i[0].isupper() for i in s.split()))


# string23('Hello, world')  # 1
# string23('John Smith')  # 2
# string23('JohnSmith')  # 1

'''Дана строка s, состоящая из целых чисел, разделённых одиночными пробелами. 
Выведите сумму этих чисел.'''


def string24(s):
    print(sum(map(int, s.split())))


# string24('10 20 30')  # 60
# string24('-1 2 -3')  # -2
# string24('0 0 10 -5 -5')  # 0

'''Дан строковый массив a. 
Объедините все элементы массива в одну строку, используя '; ' как разделитель.'''


def string25(a):
    print("; ".join(a))


# string25(['abc', 'qwe', 'asd'])  # abc; qwe; asd
# string25(['test'])  # test
# string25([])  #

'''Дана строка s, состоящая из слов, разделённых одиночными пробелами. 
Если среди слов нет слова 'class', то добавить его в конец списка слов. Вывести все слова через пробел.'''


def string26(s):
    arr = s.split()
    if 'class' not in arr:
        arr.append('class')
    print(' '.join(arr))


# string26('cclass classs')  # cclass classs class
# string26('class')  # class
# string26('')  # class

'''Дана строка s, состоящая из слов, разделённых одиночными пробелами. 
Если среди слов есть слово (одно или несколько) 'class', то удалить его. Вывести все слова через пробел.'''


def string27(s):
    # b = []
    # for w in s.split():
    #     if w != 'class':
    #         b.append(w)
    print(*[w for w in s.split() if w != 'class'])


# string27('cclass classs')  # cclass classs
# string27('class')  #
# string27('class test class')  # test

'''Дана строка s, содержащая путь к файлу. 
Вывести расширение файла и его имя.'''


def string28(s):
    inx_dot = s.rfind('.')
    ind_sls = s.rfind('/')
    print(s[inx_dot + 1:], s[ind_sls + 1: inx_dot])


# string28('/var/www/index.html')  # html index
# string28('/var/log/log.01.tar.gz')  # gz log.01.tar
# string28('Zadachi na stroki.js')  # js Zadachi na stroki
# string28('/a/b/Zadachi.na.stroki.js')  # js Zadachi.na.stroki
