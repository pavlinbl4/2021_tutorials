"""Дана строка s и число n. Создайте и выведите объект, в котором по ключу 'name' будет значение s, а по ключу 'age'
значение n. """


def obj1(s, n):
    # voc = dict(name=s, age=n)
    # print(voc)
    print({'name': s, 'age': n})


# obj1('Вася', 20)  # {name: 'Вася', age: 20} # почему в варианте ответа ключи написаны без кавычек ?
# obj1('Петя', 30)  # {name: 'Петя', age: 30}

'''Дан объект a. 
Запишите в него по ключу 'name' значение 'Вася'. Выведите объект.'''


def obj2(a):
    a['name'] = 'Вася'
    print(a)


# obj2({'age': 20})  # {age: 20, name: 'Вася'}
# obj2({'name': 'Петя', 'age': 30})  # {name: 'Вася', age: 30}
# obj2({})  # {name: 'Вася'}

'''Дан объект a. 
Выведите значение по ключам 'name' и 'age' через пробел.'''


def obj3(a):  # у меня в отете None, а не  undefined
    print(a.get('name', 'undefined'), a.get('age', 'undefined'))


# obj3({'age': 20})   # undefined 20
# obj3({'name': 'Петя', 'age': 30})  # Петя 30
# obj3({})  # undefined undefined


'''Дан объект a и строка s. 
Запишите в него по ключу s значение s, приведённое к верхнему регистру. Выведите объект.'''


def obj4(a, s):
    a[s] = s.upper()
    print(a)


# obj4({'age': 20}, 'name')  # {age: 20, name: 'NAME'}
# obj4({'name': 'Вася', 'age': 30}, 'age')  # {name: 'Вася', age: 'AGE'}
# obj4({}, '0')  # {'0': '0'}

'''Дан объект a и строка s. 
Удалите из объекта ключ 'name' и ключ s. Выведите объект.'''


def obj5(a, s):
    if 'name' in a:
        a.pop('name')
    if s in a:
        a.pop(s)
    print(a)


# obj5({'age': 20}, 'age')  # {}
# obj5({'name': 'Петя', 'age': 30}, 'age')  # {}
# obj5({'age': 20}, 'name')  # {age: 20}

'''Дан объект a с ключами 'a', и 'b' (с целочисленными значениями). 
Если значение по ключу 'a' больше, чем по ключу 'b', то увеличьте значение по ключу 'a' на значение по ключу 'b', 
иначе оба значения увеличьте на 1. Выведите объект.'''


def obj6(a):
    if a['a'] > a['b']:
        a['a'] += a['b']
    else:
        a['a'] += 1
        a['b'] += 1
    print(a)


# obj6({'a': 20, 'b': 10})  # {'a': 30, 'b': 10}
# obj6({'a': 20, 'b': 30})  # {'a': 21, 'b': 31}
# obj6({'a': 20, 'b': 20})  # {'a': 21, 'b': 21}

'''Дан объект a. 
Выведите массив из его ключей.'''


def obj7(a):
    print(list(a))


# obj7({'a': 20, 'b': 10, 0: 30})  # ['0', 'a', 'b']
# obj7({'name': 'Вася', 'age': 20})  # ['name', 'age']
# obj7({})  # []

'''Дан объект a. Выведите массив из его значений.'''


def obj8(a):
    print(list(a.values()))


# obj8({'a': 20, 'b': 10, 0: 30})  # [20, 10, 30]
# obj8({'name': 'Вася', 'age': 20})  # ['Вася', 20]
# obj8({})  # []

'''Дан объект a и массив строк keys. 
Для каждого элемента из keys проверьте, есть ли такой ключ в объекте. 
Выведите массив такой же длины, как и keys, 
состоящий из логических значений (true или false) - есть или нет такой ключ в объекте.'''


def obj9(a, keys):
    print([k in a for k in keys])


# obj9({'a': 20, 'b': 10, '0': 30}, ['b', 'x', '0'])  # [True, False, True]
# obj9({'name': 'Вася', 'age': 20}, ['age', 'age', 'name'])  # [True, True, True]
# obj9({}, ['a', 'a', 'a'])  # [False, False, False]

'''Дано число n. Создайте объект, 
ключами которого будут числа от 0 (включительно) до n (не включительно), 
а значениями числа n. Выведите объект.'''


def obj10(n):  # исходя из примеров ответа ключами должны быть строки ?
    print({str(i): n for i in range(n)})
    # voc = {i: n for i in range(n)}
    # voc = {str(i): n for i in range(n)}
    # print(voc)


# obj10(0)  # {}
# obj10(1)  # {'0': 1}
# obj10(3)  # {'0': 3, '1': 3, '2': 3}

'''Дано число n. 
Создайте объект, ключами которого будут n первых строчных букв алфавита, 
а значениями их коды в таблице ascii.'''


def obj11(n):
    x = ord("a")
    print({chr(i): i for i in range(x, x + n)})


# obj11(0)  # {}
# obj11(1)  # {'a': 97}
# obj11(3)  # {'a': 97, 'b': 98, 'c': 99}


'''Дана строка s. 
Создайте объект, ключами которого будут символы из строки s, 
а значениями их коды в таблице ascii. Выведите объект.'''


def obj12(s):
    print({i: ord(i) for i in s})


# obj12('')  # {}
# obj12('z')  # {'z': 122}
# obj12('test')  # {'t': 116, 'e': 101, 's': 115}


'''Дана строка s. 
Выведите массив, который содержит только различные символы строки s (порядок не важен).'''


def obj13(s):
    # print(list(set(s))) # проще через множество
    print(list({i: None for i in s}))


# obj13('')  # []
# obj13('abc')  # ['a', 'b', 'c']
# obj13('test')  # ['s', 't', 'e']


'''Дана строка s. 
Создайте объект, ключами которого будут символы из строки s, 
а значениями количество вхождений соответствующего символа в строку.'''


def obj14(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    print(d)


# obj14('')  # {}
# obj14('abc')  # {'a': 1, 'b': 1, 'c': 1}
# obj14('test')  # {'t': 2, 'e': 1, 's': 1}

'''Дан массив строк a и объект d (со строковыми значениями). 
Произведите замену тех элементов в массиве a, для которых есть соответствующий ключ в объекте d, 
на значения по этому ключу из объекта. Выведите модифицированный массив.'''


def obj15(a, d):
    for i in range(len(a)):
        if a[i] in d:
            a[i] = d[a[i]]
    print(a)


# obj15(['t', 'e', 's', 't'], {'t': 'a', 'e': 'b'})   # ['a', 'b', 's', 'a']
# obj15(['a', 'a', 'a'], {'a': 'b', 'b': 'a'})        # ['b', 'b', 'b']
# obj15(['t', 'e', 's', 't'], {'x': 't'})             # ['t', 'e', 's', 't']

'''Дан объект d (со строковыми значениями). 
Создайте новый объект, ключами которого будут значения d, 
а значениями - ключи d. Выведите новый объект.'''


def obj16(d):
    print({v: k for k, v in d.items()})


# obj16({'a': 'x', 'b': 'y', 'c': 'z'})  # {'x': 'a', 'y': 'b', 'z': 'c'}
# obj16({'a': 'a', 'b': 'b', 'c': 'c'})  # {'a': 'a', 'b': 'b', 'c': 'c'}
# obj16({'a': 'a', 'b': 'a', 'c': 'a'})  # {'a': 'c'}

'''Дан массив строк a чётной длины. 
Создайте объект, в котором ключами будет каждый второй элемент, начиная с первого, 
а значениями каждый второй, начиная со второго.'''


def obj17(a):  # здесь мы остановили проверку ДЗ
    # print({a[i]: a[i + 1] for i in range(0, len(a), 2)})
    print(dict(zip(a[::2], a[1::2])))


# obj17(['a', 'b'])  # {'a': 'b'}
# obj17(['a', 'a', 'b', 'b'])  # {'a': 'a', 'b': 'b'}
# obj17(['a', 'b', 'a', 'b'])  # {'a': 'b'}

'''Дан объект d с числовыми значениями. 
Выведите максимальное значение и сумму всех значений.'''


def obj18(d):
    v = d.values()
    print(v)
    print(max(v), sum(v))


# obj18({'a': 5, 'b': 7, 'c': 3})  # 7 15
# obj18({'a': -3,'b': -5, 'c': -1})  # -1 -9
obj18({'a': 10, 'a': 20, 'a': -3})  # -3 -3

'''Дан объект d с числовыми значениями. 
Выведите ключ, соответствующий максимальному значению (любой, если их несколько).'''


def obj19(d):
    # arr = []                      # 1 вариант
    # for value in d.values():
    #     arr.append(value)
    # max_value = max(arr)
    # for i in d:
    #     if d[i] == max_value:
    #         print(i)

    sorted_tupl = max(d.items(), key=lambda item: item[1])  # 2 вариант
    print(sorted_tupl[0])


# obj19({'a': 5, 'b': 7, 'c': 3})  #
# obj19({'a': -3, 'b': -5, 'c': -1})  #
# obj19({'a': 10, 'b': 20, 'b': 10})  # одинаковые ключи в словаре

'''Дан массив вида [['key1', 'value1'], ['key2', 'value2']...]. 
Создайте из него объект вида {key1: 'value1', key2: 'value2'...}.'''


def obj20(a):
    # voc = {}          # вариант 1
    # for i in a:
    #     voc[i[0]] = i[1]
    # print(voc)
    # print({i[0]: i[1] for i in a})  # вариант 2
    # print({k: v for k, v in a})
    print(dict(a))  # вариант 3


# obj20([['key1', 'value1'], ['key2', 'value2']])  #
# obj20([['a', 'b'], ['c', 'd']])  #
# obj20([['a', 'b'], ['a', 'c'], ['a', 'd']])  #


def obj21(a, b):
    # voc = {}                      # вариант 1
    # for i in range(len(a)):
    #     voc[a[i]] = b[i]
    # print(voc)

    # print({a[i]: b[i] for i in range(len(a))})  # вариант 2
    # print({k: v for k, v in zip(a, b)})  # вариант 3
    print(dict(zip(a, b)))  # вариант 4


# obj21(['key1', 'key2'], ['value1', 'value2'])
# obj21(['a', 'b'], ['c', 'd'])
# obj21(['a', 'a', 'a'], ['b', 'c', 'd'])


def obj22(a):
    # voc = {}                              # вариант 1
    # for i in a:
    #     voc[i['name']] = i['value']
    # print(voc)

    print({i['name']: i['value'] for i in a})  # вариант 2


# obj22([{'name': 'key1', 'value': 'value1'}, {'name': 'key2', 'value': 'value2'}])
# obj22([{'name': 'a', 'value': 'b'}, {'name': 'c', 'value': 'd'}])
# obj22([{'name': 'a', 'value': 'b'}, {'name': 'a', 'value': 'c'}])


def obj23(a):
    # arr = []   # вариант 1
    # for i in a:
    #     arr.append(i)
    #     arr.append(a[i])
    # print(arr)
    # arr = []   # вариант 2
    # for i in a.items():
    #     arr += list(i)
    # print(arr)
    # arr = [0] * (len(a) * 2)
    # i = 0
    # for k, v in a.items():
    #     arr[i] = k
    #     arr[i + 1] = v
    #     i += 2
    # print(arr)
    arr = [0] * (len(a) * 2)
    arr[::2] = a
    arr[1::2] = a.values()
    print(arr)


# obj23({'key1': 'value1', 'key2': 'value2'})
# obj23({'a': 'b', 'c': 'd'})
# obj23({'a': 'b', 'a': 'c'})



def obj24(a):
    voc = {}
    for i in a:
        voc[i['id']] = i
    print(voc)


# a = [
#   {'id': 1, 'name': 'Vasya'},
#   {'id': 2, 'name': 'Petya'},
# ]
# obj24(a)


def obj25(a, b):
    lst = []
    for i in range(len(b)):
        lst.append(dict(zip(a, b[i])))
    print(lst)


a = ['id', 'name', 'age']
b = [
  [1, 'Vasya', 20],
  [2, 'Petya', 30],
]
obj25(a, b)





• obj27
Отсортировать по имени
ввод:
[
{'id': 1, 'name': 'Vasya', 'age': 20},
{'id': 2, 'name': 'Petya', 'age': 30},
{'id': 3, 'name': 'Ivan', 'age': 20},
{'id': 4, 'name': 'Fedya', 'age': 30},
]
вывод:
[
{'id': 4, 'name': 'Fedya', 'age': 30},
{'id': 3, 'name': 'Ivan', 'age': 20},
{'id': 2, 'name': 'Petya', 'age': 30},
{'id': 1, 'name': 'Vasya', 'age': 20},
]
==============
• obj28
Разделить на активных и неактивных
ввод:
[
{'id': 1, 'active': False},
{'id': 2, 'active': True},
{'id': 3, 'active': True},
{'id': 4, 'active': False},
]
вывод:
[
{'id': 2, 'active': True},
{'id': 3, 'active': True}
]
[
{'id': 1, 'active': False},
{'id': 4, 'active': False}
]
==============
• obj29
Разделить на возрастные группы по десяткам (0-9, 10-19, 20-29, 30-39...)
ввод:
[
{'id': 1, 'name': 'Vasya', 'age': 15},
{'id': 2, 'name': 'Petya', 'age': 20},
{'id': 3, 'name': 'Ivan', 'age': 25},
{'id': 4, 'name': 'Fedya', 'age': 30},
]
вывод:
{
'10-19': [
{'id': 1, 'name': 'Vasya', 'age': 15}
],
'20-29': [
{'id': 2, 'name': 'Petya', 'age': 20},
{'id': 3, 'name': 'Ivan', 'age': 25}
],
'30-39': [
{'id': 4, 'name': 'Fedya', 'age': 30}
],
}
==============
• obj30
ввод:
[
{'id': 1, 'name': 'Vasya', 'age': 15},
{'id': 2, 'name': 'Petya', 'age': 20},
{'id': 3, 'name': 'Ivan', 'age': 25},
{'id': 4, 'name': 'Fedya', 'age': 30},
]
вывод:
{
'id': [1, 2, 3, 4],
'name': ['Vasya', 'Petya', 'Ivan', 'Fedya'],
'age': [15, 20, 35, 30]
}
==============
• obj31
ввод:
[
['key1', 'value1', 'value2', 'value3'],
['key2', 'value2', 'value4'],
['key3', 'value3', 'value5']
]
вывод:
{
'key1': ['value1', 'value2', 'value3'],
'key2': ['value2', 'value4'],
'key3': ['value3', 'value5']
}
==============
• obj32
ввод:
{
'key1': ['value1', 'value2', 'value3'],
'key2': ['value2', 'value4'],
'key3': ['value3', 'value5']
}
вывод:
[
['key1', 'value1', 'value2', 'value3'],
['key2', 'value2', 'value4'],
['key3', 'value3', 'value5']
]
==============
• obj33
ввод:
[
['k1', 'v1'],
['k1', 'v2'],
['k2', 'v2'],
['k2', 'v3'],
['k3', 'v1'],
['k3', 'v2'],
['k3', 'v3'],
]
вывод:
{
'k1': ['v1', 'v2'],
'k2': ['v2', 'v3'],
'k3': ['v1', 'v2', 'v3'],
}
==============
• obj34
ввод:
{
'key1': ['value1', 'value2', 'value3'],
'key2': ['value2', 'value4'],
'key3': ['value3', 'value5']
}
вывод:
{
'value1': ['key1'],
'value2': ['key1', 'key2'],
'value3': ['key1', 'key3'],
'value4': ['key2'],
'value5': ['key3'],
}
==============
• obj35
ввод:
[
['key1', 'value1', 'value2', 'value3'],
['key2', 'value2', 'value4'],
['key3', 'value3', 'value5']
]
вывод:
[
['value1', 'key1'],
['value2', 'key1', 'key2'],
['value3', 'key1', 'key3'],
['value4', 'key2'],
['value5', 'key3'],
]