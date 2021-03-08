# https://stepik.org/lesson/23897/step/1?adaptive=true&unit=6423

rez = []
shift = int(input())
text = input()
text = text.strip()  # убраем пробелы в конце и начале
last = ord("🙏")
first = ord("😀")
for x in text:
    dd = ord(x) - first # индекс смайлика в таблице
    new_dd = (dd + shift ) % 80 + first
    rez.append(chr(new_dd))
print("Result: " + '"' + ''.join(rez) + '"')