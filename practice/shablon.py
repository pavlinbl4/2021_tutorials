import pyperclip
import requests
from bs4 import BeautifulSoup
from take_tasks import task_names,task_texts, task_input, answers
lesson = task_names[0].text[:-1]
number = len(task_names)
text = ''

for i in range(0,number):

    case = task_texts[i].text.replace("\(", '')
    case = case.replace("\)", "")
    # text += f""""{case}"""\n\n\ndef {lesson}{i + 1}():\n    pass\n\n\n{lesson}{i + 1}()\n{lesson}{i + 1}()\n{lesson}{i + 1}()\n\n\n"
    # print(f""""{case}"""\n\n\ndef {lesson}{i + 1}():\n    pass\n\n\n{lesson(task_input[i][0])}{i + 1}()\n{lesson(task_input[i][1])}{i + 1}()\n{lesson(task_input[i][2])}{i + 1}()\n\n\n")
    text += f'# Задача_{i + 1}\n'
    text += f""""{case}"""\n\n\ndef {lesson}{i + 1}():\n"
    # print(f""""{case}"""\n\n\ndef {lesson}{i + 1}():")
    text += f"    pass\n\n\n\n"
    # print(f"    pass\n\n\n")
    text += f'{lesson}{i + 1}({task_input[i][0]})   # {answers[i][0]}\n'
    # print(f'{lesson}{i + 1}({task_input[i][0]})   # {answers[i][0]}')
    text += f'{lesson}{i + 1}({task_input[i][1]})   # {answers[i][1]}\n'
    # print(f'{lesson}{i + 1}({task_input[i][1]})   # {answers[i][1]}')
    text += f'{lesson}{i + 1}({task_input[i][2]})   # {answers[i][2]}\n'
    # print(f'{lesson}{i + 1}({task_input[i][2]})   # {answers[i][2]}')
    text += f'\n\n\n'
    pyperclip.copy(text)
    print(text)
