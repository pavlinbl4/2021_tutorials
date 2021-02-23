# https://stepik.org/lesson/21633/step/1?adaptive=true&unit=5133

# roman_to_dec = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# dec_to_roman = {}
# for i in roman_to_dec:
#     dec_to_roman.setdefault(roman_to_dec[i],i)
# print(dec_to_roman)
dec_to_roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
data = int(input())#1984
data = list(str(data))

data.reverse()
itog = []
for i in range(len(data)):
    digit = data[i] + "0" * i
    if int(digit) in dec_to_roman:
        itog.append(dec_to_roman[int(digit)])
    elif digit[0] == "9":
        part1 = int("1" + "0" * (len(digit) - 1))
        part2 = int("1" + "0" * (len(digit)))
        itog.append(dec_to_roman[part2])
        itog.append(dec_to_roman[part1])
    elif digit[0] == "4":
        part1 = int("1" + "0" * (len(digit) - 1))
        part2 = int("5" + "0" * (len(digit) - 1))
        itog.append(dec_to_roman[part2])
        itog.append(dec_to_roman[part1])
    elif 1 <= int(digit[0]) <= 3:
        for i in range(int(digit[0])):
            part = int("1" + "0" * (len(digit) - 1))
            itog.append(dec_to_roman[part])
    elif 6 <= int(digit[0]) <= 8:
        part1 = int("1" + "0" * (len(digit) - 1))
        part2 = int("5" + "0" * (len(digit) - 1))
        for i in range(int(digit[0]) - 5):
            itog.append(dec_to_roman[part1])
        itog.append(dec_to_roman[part2])

itog.reverse()
print(*itog, sep="")
