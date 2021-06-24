"""
удаление пробелов в строке с помощью split join
"""

text = '  AAA    777      6 99 zzz  z '
text = text.split()
print(text)
rezult = " ".join(text)
print(rezult)