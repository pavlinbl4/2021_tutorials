""" версия 3 изменил папку, куда будут сохраняться изображения,
замечен следующий недостаток  я не могу парсить страницы предыдущих
месяцев
"""

from time import sleep
import requests
from bs4 import BeautifulSoup
import os
import pandas as pd


def date_convert(day): # функция преоразует введенный номер месяца в его название
    voc = {"января": '01', "февраля": '02', "марта": '03', "апреля": '04', "мая": '05', "июня": '06', "октября": '10',
           "ноября": '11', "декабря": '12'}
    new_date = day.split()
    if new_date[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        day0 = '0' + new_date[0]
    else:
        day0 = new_date[0]
    day = f'{new_date[2]}-{voc[new_date[1]]}-{day0}'
    return day


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4200.0 Iron Safari/537.36"
}

print("ENTER NUMBER OF MONTH")
month = str(input())
if len(month) < 2:
    month = '0' + month

number_pages = 5  # int(input())

os.makedirs("pages", exist_ok=True)  # создаю папку для сохранения страниц, если папка есть, то она остается

articles_dict = {}  # словарь для сохраннения информации
count = 1

for x in range(1,number_pages + 1):  # цикл проходит по страницам и сохраняет их как html файлы с префиксами номера страницы

    # модуль обращающийся к сайту

    url = f"https://newprospect.ru/?PAGEN_1={x}"
    req = requests.get(url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')

    articles_date = soup.select("div .articles-small .date")  # дата публикации

    articles_title = soup.select("div .main-left .title a")  # находим заголовки статей

    image_links = soup.select("div .main-left .image img ")  # список со ссылками на изображение

    for i in range(len(articles_date) - 1, -1,
                   -1):  # в этом цикле перебираем наши списки с названием датой и ссылкой на фото
        count += 1
        if f"2021-{month}" in date_convert(articles_date[i].text):  # создаю фильтр для отсечения прошлого масяца

            # print(articles_date[i].text)
            # print(articles_title[i].text)
            # print("https://newprospect.ru" + image_links[i].get("src"))
            os.makedirs(f"/Volumes/big4photo/Documents/NewProspect/{month}", exist_ok=True)
            r = requests.get("https://newprospect.ru" + image_links[i].get("src"), stream=True)
            with open(
                    f"/Volumes/big4photo/Documents/NewProspect/{month}/{date_convert(articles_date[i].text)}__{articles_title[i].text}.JPG",
                    "bw") as f:
                for chunk in r.iter_content(9000):
                    f.write(chunk)
            articles_dict.setdefault("Date", []).append(date_convert(articles_date[i].text))
            articles_dict.setdefault("Title", []).append(articles_title[i].text)
            articles_dict.setdefault("Links", []).append("https://newprospect.ru" + image_links[i].get("src"))
    for i in range(len(articles_dict["Date"])):
        print(articles_dict["Date"][i], articles_dict["Title"][i])
    df = pd.DataFrame(articles_dict)
    df.to_excel('NP.xlsx', sheet_name='Links', index=False)
