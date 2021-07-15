"""Text39.
Дано целое число K и текстовый файл, содержащий текст, выровненный по левому краю.
Абзацы выделяются в нем с помощью красной строки ( начальных пробелов), а пустых строк нет.
Отформатировать текст так, чтобы его ширина не превосходила позиций,
и выровнять текст по левому краю, сохранив деление на абзацы.
Пробелы в конце строк удалить. Сохранить отформатированный текст в новом текстовом файле."""


def analize39(txt_file, k):
    def print_paragraph(paragraph):
        pass

    paragraph = []
    with open(txt_file, 'r') as text_in:
        line = text_in.readline().rstrip()
        if line.startswith("     "):
            paragraph.append(line)
        else:
            paragraph.append(line)
        for line2 in text_in:
            line2 = line2.rstrip()
            if line2.startswith("     "):
                print(paragraph)
                paragraph.clear()
                paragraph.append(line2)
            else:
                paragraph.append(line2)
            line = line2


txt_file = "/Users/evgeniy/PycharmProjects/2021_tutorials/practice" \
           "/Cool_code/work_with_text_files/24-39 Анализ и форматирование текста/39in.txt"
analize39(txt_file, 30)
