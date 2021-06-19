"""Text1.
Дано имя файла и целые положительные числа N и  K.
Создать текстовый файл с указанным именем и записать в него N строк,
каждая из которых состоит из символов K «*» (звездочка)."""


def text1(n, k):
    with open('text1.txt', 'w') as tutorial:
        for i in range(n):
            print("*" * k, file=tutorial)


# text1(3,7)

"""Text2. 
Дано имя файла и целое число 0<K<27. 
Создать текстовый файл с указанным именем и записать в него строк: 
первая строка должна содержать строчную (то есть маленькую) латинскую букву «a», 
вторая — буквы «ab», третья — буквы «abc» и т. д.; 
последняя строка должна содержать начальных строчных латинских букв в алфавитном порядке."""


def text2(k,name):
    with open(f'{name}.txt', 'w') as tutorial:
        for i in range(1, k + 1):
            line = [chr(ord('a') + x) for x in range(i)]
            print(''.join(line), file=tutorial)


# text2(26,'text2')

"""Text3. 
Дано имя файла и целое число 0<K<27. 
Создать текстовый файл с указанным именем и записать в него N строк:"""


def text3(n,name):
    with open(f'{name}.txt', 'w') as tutorial:
        for i in range(1, n + 1):
            line1 = [chr(ord('A') + x) for x in range(i)]
            line2 = "*" * (n - i)
            print(''.join(line1)+line2, file=tutorial)


# text3(26,'text3')

def text4(name):
    with open(f'{name}.txt', 'r') as tutorial:
        line_count = 0
        symbols_count = 0
        for line in tutorial:
            line_count += 1
            # print(f'количество символов в строке {len(line) - 1}')
            symbols_count += len(line) - 1
    print(f'количество строк {line_count},'
          f'количество символов {symbols_count}')

# text4('song')

"""Text5. 
Дана строка и текстовый файл. Добавить строку в конец файла."""

def text5(name, add_line):
    with open(f'{name}.txt', 'a') as tutorial:
        # print(file=tutorial)
        print(add_line, file=tutorial)

# text5('song','Федор Чистяков')

"""Text6. 
Даны два текстовых файла. 
Добавить в конец первого файла содержимое второго файла."""

def text6(name1, name2):
    with open(f'{name2}.txt', 'r') as add_text:
        for line in add_text:
            with open(f'{name1}.txt', 'a') as tutorial:
                print(line.strip(), file=tutorial)

# text6('song','text1')


def text7(name,add_line):
    with open(f'{name}.txt', 'r') as tutorial:
        all_lines = tutorial.readlines()
        all_lines.insert(0,add_line + '\n')
    with open(f'{name}.txt', 'w') as tutorial:
        for words in all_lines:
            tutorial.write(words)



# text7('song','Человек и кошка')


"""Text8. 
Даны два текстовых файла. 
Добавить в начало первого файла содержимое второго файла."""
def text8(file1,file2):
    all_to_insert = []
    all_base_text = []
    with open(file2,'r') as additional_file:
        all_to_insert = additional_file.readlines()
    with open(file1, 'r') as main_file:
        all_base_text = main_file.readlines()
        all_to_insert = all_to_insert + all_base_text
    with open(file1, 'w') as main_file:
        for lines in all_to_insert:
            main_file.write(lines)



# text8('main.txt','song.txt')


"""Text9. 
Дано целое число и текстовый файл. 
Вставить пустую строку перед строкой файла с номером . 
Если строки с таким номером нет, то оставить файл без изменений.
(считаю что нумерация строк начинается с еденицы)
"""
def text9(file1,k):

    with open(file1,'r') as main_file:
        all_lines = main_file.readlines()
    if k < len(all_lines):
        all_lines.insert(k -1,'\n')
        with open(file1,'w') as main_file:
            for lines in all_lines:
                main_file.write(lines)


# text9('file_for_9.txt',2)


"""Text10. 
Дано целое число и текстовый файл. 
Вставить пустую строку после строки файла с номером . 
Если строки с таким номером нет, то оставить файл без изменений."""

def text10(file1,k):

    with open(file1,'r') as main_file:
        all_lines = main_file.readlines()
    if k < len(all_lines):
        all_lines.insert(k ,'\n')
        with open(file1,'w') as main_file:
            for lines in all_lines:
                main_file.write(lines)


# text10('file_for_9.txt',2)

