"""  Напишите рекурсивную функцию is_power(n), которая возвращает True,
если переданное натуральное число является степенью двойки, и False иначе.
Кроме функции ничего писать не нужно."""

def is_power(n):
    if n < = 2:
        return True
    else:
        return False

    return is_power(n/2)


print(is_power(3))

