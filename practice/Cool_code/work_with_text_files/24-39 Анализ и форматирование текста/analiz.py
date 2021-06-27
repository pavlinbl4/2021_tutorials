"""Text24.
Дан текстовый файл. Найти количество абзацев в тексте,
если абзацы отделяются друг от друга одной или несколькими пустыми строками."""

def analize24(file):
    with open(file,'r') as text:
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

def analize25(file,k):
    with open(file, 'r') as text_in, open('25.txt','w') as text_out:
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
    with open(file,'r') as text:
        lines = text.readlines()
        for line in lines:
            if line.startswith("     ") and line.strip() != '':
                abzats +=1
    print(abzats)

# analize26("start1.txt")

"""Text27. 
Дано целое число  K и текстовый файл. 
Удалить из файла абзац с номером (абзацы выделяются с помощью красной строки — см. задание Text26). 
Пустые строки между абзацами не учитывать и не удалять. 
Если абзац с данным номером отсутствует, то оставить файл без изменений."""

def analize27(file,k):