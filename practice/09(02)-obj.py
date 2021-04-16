from pprint import pprint


# Сгруппировать по возрасту

def obj26(a):
    voc = {}
    for i in a:
        voc.setdefault(i['age'], [])
        voc[i['age']].append(i)
    print(voc)



a = [
    {'id': 1, 'name': 'Vasya', 'age': 20},
    {'id': 2, 'name': 'Petya', 'age': 30},
    {'id': 3, 'name': 'Ivan', 'age': 20},
    {'id': 4, 'name': 'Fedya', 'age': 30},
]

""" вывод:
{
20: [
{'id': 1, 'name': 'Vasya', 'age': 20},
{'id': 3, 'name': 'Ivan', 'age': 20}
],
30: [
{'id': 2, 'name': 'Petya', 'age': 30},
{'id': 4, 'name': 'Fedya', 'age': 30}
]
}
"""


# def obj27(n):
    # pprint(sorted(n, key=lambda x: x['name']))


# Отсортировать по имени
# ввод:
# n = [{'id': 1, 'name': 'Vasya', 'age': 20},
#     {'id': 2, 'name': 'Petya', 'age': 30},
#     {'id': 3, 'name': 'Ivan', 'age': 20},
#     {'id': 4, 'name': 'Fedya', 'age': 30}]
# obj27(n)



# Разделить на активных и неактивных
def obj28(arr):
    print([x for x in arr if x['active'] == True],
           [x for x in arr if x['active'] == False],sep = "\n")




# arr = [
#   {'id': 1, 'active': False},
#   {'id': 2, 'active': True},
#   {'id': 3, 'active': True},
#   {'id': 4, 'active': False},
# ]
# obj28(arr)


# вывод:
# [
#   {'id': 2, 'active': True},
#   {'id': 3, 'active': True}
# ]
# [
#   {'id': 1, 'active': False},
#   {'id': 4, 'active': False}
# ]

def obj29(arr):
    kkeys = {}
    for i in arr:
        kkey = f"{i['age']//10 * 10}-{i['age']//10 * 10 + 9}"
        kkeys.setdefault(kkey,[])
        kkeys[kkey].append(i)
    print("Task_29")
    print("-" * 60)
    pprint(kkeys)
    print("-" * 60)

arr = [
  {'id': 1, 'name': 'Vasya', 'age': 15},
  {'id': 2, 'name': 'Petya', 'age': 20},
  {'id': 3, 'name': 'Ivan', 'age': 25},
  {'id': 4, 'name': 'Fedya', 'age': 30},
]
obj29(arr)
"""
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
"""
def obj30(arr):
    answer = {}
    for i in arr[0].keys():
        answer.setdefault(i,[])
    for i in answer:
        for item in arr:
            answer[i].append(item[i])
    print("Task_30")
    print("-" * 60)
    pprint(answer, sort_dicts=False)
    print("-" * 60)



arr = [
  {'id': 1, 'name': 'Vasya', 'age': 15},
  {'id': 2, 'name': 'Petya', 'age': 20},
  {'id': 3, 'name': 'Ivan', 'age': 25},
  {'id': 4, 'name': 'Fedya', 'age': 30},
]
obj30(arr)
"""
вывод:
{
  'id': [1, 2, 3, 4],
  'name': ['Vasya', 'Petya', 'Ivan', 'Fedya'],
  'age': [15, 20, 35, 30]
}
"""
def obj31(arr):
    answer = {arr[i][0]: arr[i][1:] for i in range(len(arr))}
    print("Task_31")
    print("-" * 60)
    pprint(answer)
    print("-" * 60)




arr = [
    ['key1', 'value1', 'value2', 'value3'],
    ['key2', 'value2', 'value4'],
    ['key3', 'value3', 'value5']
]
obj31(arr)
"""
вывод:
{
    'key1': ['value1', 'value2', 'value3'],
    'key2': ['value2', 'value4'],
    'key3': ['value3', 'value5']
}
"""

def obj32(voc):
    answer = []
    for i in voc:
        voc[i].insert(0,i)
        answer.append(voc[i])

    print("Task_32")
    print("-" * 60)
    pprint(answer)
    print("-" * 60)

voc = {
    'key1': ['value1', 'value2', 'value3'],
    'key2': ['value2', 'value4'],
    'key3': ['value3', 'value5']
}
obj32(voc)
# вывод:
# [
#     ['key1', 'value1', 'value2', 'value3'],
#     ['key2', 'value2', 'value4'],
#     ['key3', 'value3', 'value5']
# ]

def obj33(arr):
    voc = {}
    for i in arr:
        voc.setdefault(i[0],[])
        voc[i[0]].append(i[1])


    print("Task_33")
    print("-" * 60)
    print(voc)
    print("-" * 60)


arr = [
    ['k1', 'v1'],
    ['k1', 'v2'],
    ['k2', 'v2'],
    ['k2', 'v3'],
    ['k3', 'v1'],
    ['k3', 'v2'],
    ['k3', 'v3'],
]
obj33(arr)
"""
вывод:
{
    'k1': ['v1', 'v2'],
    'k2': ['v2', 'v3'],
    'k3': ['v1', 'v2', 'v3'],
}
"""
def obj34(voc):
    print("Task_34")
    print("-" * 60)
    print(answer)
    print("-" * 60)

voc = {
    'key1': ['value1', 'value2', 'value3'],
    'key2': ['value2', 'value4'],
    'key3': ['value3', 'value5']
}
"""вывод:
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
"""