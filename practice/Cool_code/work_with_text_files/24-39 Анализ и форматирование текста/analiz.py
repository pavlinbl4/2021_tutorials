import re

"""Text24.
Дан текстовый файл. Найти количество абзацев в тексте,
если абзацы отделяются друг от друга одной или несколькими пустыми строками."""


def analize24(file):
    with open(file, 'r') as text:
        line = text.readline()
        if line.strip() == '':
            paragraf = 0
        else:
            paragraf = 1
        for line2 in text:
            if line.strip() == '' and line2.strip() != '':
                paragraf += 1
            line = line2
    print(paragraf)


# analize24("start1.txt")


"""Text25. 
Дано целое число и текстовый файл. 
Удалить из файла абзац с номером (абзацы отделяются друг от друга одной или несколькими пустыми строками). 
Пустые строки, предшествующие и следующие за удаляемым абзацем, не удалять. 
Если абзац с данным номером отсутствует, то оставить файл без изменений."""


def analize25(file, k):
    with open(file, 'r') as text_in, open('25.txt', 'w') as text_out:
        line1 = text_in.readline()
        if line1.strip() == '':
            paragraf = 0
        else:
            paragraf = 1
        if paragraf != k or line1.strip() == '':
            text_out.write(line1)
        for line in text_in:
            if line.strip() == '' and line1.strip() != '':
                paragraf += 1
            line1 = line
            if paragraf != k or line.strip() == "":
                text_out.write(line)


# analize25("start1.txt",3)

"""Text26. 
Дан текстовый файл. Найти количество абзацев в тексте, 
если первая строка каждого абзаца начинается с пробелов («красная строка»). 
Пустые строки между абзацами не учитывать."""


def analize26(file):
    abzats = 0
    with open(file, 'r') as text:
        lines = text.readlines()
        for line in lines:
            if line.startswith("     ") and line.strip() != '':
                abzats += 1
    print(abzats)


# analize26("start1.txt")

"""Text27. 
Дано целое число  K и текстовый файл. 
Удалить из файла абзац с номером (абзацы выделяются с помощью красной строки — см. задание Text26). 
Пустые строки между абзацами не учитывать и не удалять. 
Если абзац с данным номером отсутствует, то оставить файл без изменений."""


def analize27(file, k):
    abzats = 0
    with open(file, 'r') as text_in, open('27.txt', 'w') as text_out:
        line1 = text_in.readline()
        if line1.startswith("     "):
            abzats += 1
        if abzats != k or line1.strip() == '':
            text_out.write(line1)
        for line2 in text_in:
            if line2.startswith("     "):
                abzats += 1
            if abzats != k or line2.strip() == '':
                text_out.write(line2)

        text_out.write('\n\n"Антракт, негодяи!"')


# analize27("start1.txt",2)

"""Text28. 
Дан текстовый файл. Абзацы выделяются в нем с помощью красной строки (см. задание Text26), а пустых строк нет. 
Вставить между соседними абзацами по одной пустой строке (в начало и конец файла пустые строки не добавлять)."""


def analize28(file):
    with open(file, 'r') as text_in, open('28.txt', 'w') as text_out:
        line1 = text_in.readline()
        text_out.write(line1)
        for line2 in text_in:
            if line2.startswith("     ") and line1.strip() != '':
                text_out.write('\n')
                text_out.write(line2)
            else:
                text_out.write(line2)
        text_out.write('\n"Антракт, негодяи!"')


# analize28('input28.txt')

"""Text29. 
Дан текстовый файл. Вывести первое слово текста наибольшей длины. 
Словом считать набор символов, не содержащий пробелов и ограниченный пробелами или началом/концом строки."""


def analize29(file):
    voc_counter = {}
    with open(file, 'r') as text_in:
        lines = text_in.read()
    lines = lines.split()
    for word in lines:
        key_count = len(word)
        if key_count not in voc_counter:
            voc_counter[key_count] = word
    print(voc_counter[max(voc_counter)])


# analize29('input28.txt')

"""Text30. 
Дан текстовый файл. Вывести последнее слово текста наименьшей длины. 
Словом считать набор символов, не содержащий пробелов и ограниченный пробелами или началом/концом строки."""


def analize30(file):
    voc_counter = {}
    with open(file, 'r') as text_in:
        lines = text_in.read()
    lines = lines.split()
    for word in lines:
        key_count = len(word)
        voc_counter[key_count] = word
    print(voc_counter[min(voc_counter)])


# analize30('start1.txt')


"""Text31. 
Дано целое число и текстовый файл. 
Создать строковый файл и записать в него все слова длины из исходного файла. 
Словом считать набор символов, не содержащий пробелов, знаков препинания и ограниченный пробелами, 
знаками препинания или началом/концом строки. 
Если исходный файл не содержит слов длины K, то оставить результирующий файл пустым."""


def analize31(file, k):
    with open(file, 'r') as text_in:
        lines = text_in.read()
        optimized_text = re.findall('\w+', lines)
    with open('31.txt', 'w') as text_out:
        for word in optimized_text:
            if len(word) == k:
                text_out.write(word)
                text_out.write('\n')


# analize31('start1.txt', 5 )


"""Text33. 
Дан символ — строчная (маленькая) русская буква и текстовый файл. 
Создать строковый файл и записать в него все слова из исходного файла, содержащие хотя бы одну букву (прописную или строчную). 
Словом считать набор символов, не содержащий пробелов, знаков препинания и ограниченный пробелами, знаками препинания или началом/концом строки. 
Если исходный файл не содержит подходящих слов, то оставить результирующий файл пустым."""


def analize33(file, k):
    with open(file, 'r') as text_in:
        lines = text_in.read()
        optimized_text = re.findall('\w+', lines)
        with open('33.txt', 'w') as text_out:
            for word in optimized_text:
                if k in word.lower():
                    text_out.write(word)
                    text_out.write('\n')


# analize33('start1.txt', "с" )

"""Text34. 
Дан текстовый файл, содержащий текст, выровненный по левому краю. 
Выровнять текст по правому краю, добавив в начало каждой непустой строки нужное количество пробелов 
(ширину текста считать равной 50)."""


def analize34(file):
    with open(file, 'r') as text_in, open('34.txt', 'w') as text_out:
        for line in text_in:
            text_out.write(line.rjust(50))


# analize34('33.txt')

"""Text35. 
Дан текстовый файл, содержащий текст, выровненный по левому краю. 
Выровнять текст по центру, добавив в начало каждой непустой строки нужное количество пробелов 
(ширину текста считать равной 50 ). Строки нечетной длины перед центрированием дополнять слева пробелом."""


def analize35(file):
    with open(file, 'r') as text_in, open('35.txt', 'w') as text_out:
        for line in text_in:
            if len(line) % 2 == 0:
                line = " " + line
            print(line.strip().center(50), file=text_out)
            # text_out.write(line.center(50)) # странно но так выравнивание не получается


# analize35('33.txt')


"""Text36. 
Дан текстовый файл, содержащий текст, выровненный по правому краю. 
Выровнять текст по центру, удалив из каждой непустой строки половину начальных пробелов. 
В строках с нечетным количеством начальных пробелов перед центрированием удалять первый начальный пробел."""


def analize36(file):
    with open(file, 'r') as text_in, open('36.txt', 'w') as text_out:
        lines = text_in.readlines()
        for line in lines:
            if line.strip() != "":
                space_count = len(line) - len(line.strip())  # количество пробелов перед текстом
                if space_count % 2 == 0:
                    short_space = space_count // 2 + len(line.strip())
                else:
                    short_space = (space_count - 1) // 2 + len(line.strip())
                line = line.strip()
                line = line.center(short_space, "*")
                text_out.write(f'{line}   letters - {len(line.strip())}, spaces - {space_count} \n')


            else:
                text_out.write("\n")


# analize36('36_out.txt')

"""Text37. 
Дан текстовый файл, содержащий текст, выровненный по левому краю. 
Абзацы текста разделяются одной пустой строкой. Выровнять текст по ширине (то есть и по левому, и по правому краю), 
увеличив в каждой непустой строке (кроме последних строк абзацев) количество пробелов между словами, 
начиная с последнего пробела в строке (ширину текста считать равной 50 )."""


def analize37(file):
    def add_spases(line):
        if line.strip() == "":
            return line
        else:
            probel_to_add = 55 - len(line)  # количество пробелов, которое нужно добавить
            words = line.split()  # преобразую строку в список
            count = 0
            while count <= probel_to_add: # начиная с последнего слова в списке добавляю звездочку перед словои
                for i in range(len(words) - 1, 0, -1):
                    if count <= probel_to_add: # если количество звездочек достигло нужного количества то выходим из цикла
                        words[i] = " " + words[i]
                        count += 1
                    else:
                        break
            new_line = " ".join(words)
            return new_line

    with open(file, 'r') as text_in, open('37.txt', 'w') as text_out:
        line1 = text_in.readline()
        for line2 in text_in:
            if line2.strip() != "":
                line1 = add_spases(line1)
            print(line1.strip(), file=text_out)
            # text_out.write(line1)
            line1 = line2
        print(line2.strip(), file=text_out)


# analize37('36_input.txt')
