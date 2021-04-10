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

# obj26(a)

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

def obj27(n):
    arr = sorted([i['name'] for i in n])
    print([x for x in n if ])

#Отсортировать по имени
#ввод:
n =[
{'id': 1, 'name': 'Vasya', 'age': 20},
{'id': 2, 'name': 'Petya', 'age': 30},
{'id': 3, 'name': 'Ivan', 'age': 20},
{'id': 4, 'name': 'Fedya', 'age': 30},
]
obj27(n)




"""вывод:
[
{'id': 4, 'name': 'Fedya', 'age': 30},
{'id': 3, 'name': 'Ivan', 'age': 20},
{'id': 2, 'name': 'Petya', 'age': 30},
{'id': 1, 'name': 'Vasya', 'age': 20},
]
"""
