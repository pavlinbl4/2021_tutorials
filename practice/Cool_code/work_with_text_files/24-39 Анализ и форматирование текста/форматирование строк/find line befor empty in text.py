"""
вывести строки текста идущие после пустой строки
"""

def empty_line(file):
    with open(file, "r") as input_file:
        line1 = input_file.readline()
        for line2 in input_file:
            if line1.strip() == "" and line2.strip() != "":
                print(line2.strip())
            line1 = line2

"""
вывести строки текста идущие перед пустой строкой   
"""

def empty_line2(file):
    with open(file, "r") as input_file:
        line1 = input_file.readline()
        for line2 in input_file:
            if line1.strip() != "" and line2.strip() == "":
                print(line1.strip())
            line1 = line2



"""
вывести строки текста кроме строк перед пустой строкой   
"""

def empty_line3(file):

    with open(file, "r") as input_file:
        line1 = input_file.readline()
        for line2 in input_file:
            if line2.strip() != "":
                line1 = "@"+line1
            print(line1.strip())
            line1 = line2
        print(line2)


empty_line3(
    "/Users/evgeniy/PycharmProjects/2021_tutorials/practice/Cool_code/work_with_text_files/24-39 Анализ и форматирование текста/28.txt")
