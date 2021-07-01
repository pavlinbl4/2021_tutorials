"""
парсер для новой версии Нового проспекта создает csv файл с данными по опубликованным фото
"""

from bs4 import BeautifulSoup
import os
import requests
import csv

def get_html(url):
    req = requests.get(url)
    return req.text

def write_csv(data):
    with open("NP.csv",'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow((data["date"],data["name"],data["url"]))

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all('div', class_="l-page__main-news--item")
    for title in articles:
        article_date = title.find(class_="l-page__main-news--date").text.split()[-3:]  # дата публикации
        article_name = title.find('div', class_="l-page__main-news--title").text  # заголовки статей
        image_link = f'https://newprospect.ru{title.find("img").get("src")}'  # ссылка на изображение
        article_date_lookfine = " ".join(article_date)
        data = {"date":article_date_lookfine,
                "name":article_name,
                "url":image_link}
        write_csv(data)


def main():
    url = "https://newprospect.ru"
    for i in range(5):
        get_data(get_html(url))
        soup = BeautifulSoup(get_html(url), 'lxml')
        url = "https://newprospect.ru"+soup.find('li',class_='l-nav__pagination-item next').find('a').get('href')







if __name__ == '__main__':
    main()







