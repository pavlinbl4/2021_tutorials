import requests
from bs4 import BeautifulSoup
import pprint

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4200.0 Iron Safari/537.36"
}

url = "https://zadachi.vindover.ru"

try:
    # req = requests.get(url, headers=headers)
    # src = req.text
    #
    #
    # with open(f"pages/index.html", "w") as file: # сохраняем страницы для  работы
    #     file.write(src)
    with open(f"pages/index.html", "r") as file: # открываю файл для обработки
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')

    task_names = soup.select("#collapse-10 h4") # получаю название задачи
    task_texts = soup.select("#collapse-10 .card-body .task.mb-4>div:nth-child(2)") # текст задачи
    examples = soup.select("#collapse-10 .card-body .task.mb-4>div:nth-child(5) .ofxa") # входные данные, надо придумать как из отсортировать

    task_input = [examples[i].text for i in range(0,len(examples), 2)] # каждое второе значение  - это данные на вход
    answers =  [examples[i].text for i in range(1,len(examples), 2)] # а это решения


    task_input = [task_input[i: i + 3] for i in range(0, len(task_input), 3)]  # создаю вложенные списки на каждую задачу
    answers = [answers[i: i + 3] for i in range(0, len(answers), 3)]
    # for i in answers:
    #     print(i)





    # for i in range(len(task_names)): # блок проверки данных не удалаять
    #     print(task_names[i].text)
    #     print(task_texts[i].text)
    #     print(task_input[i][0],task_input[i][1],task_input[i][3])
    #     print(answers[i][0])





except Exception as ex:
    print(ex)
