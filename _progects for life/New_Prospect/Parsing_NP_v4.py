"""
скачать все опубликованные фото за месяц
"""

from bs4 import BeautifulSoup
import os
import requests

def get_html(url):
    req = requests.get(url)
    return req.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all('div', class_="l-page__main-news--item")
    for title in articles:
        article_date = title.find(class_="l-page__main-news--date").text.split()[-3:]  # дата публикации
        article_name = title.find('div', class_="l-page__main-news--title").text  # заголовки статей
        image_link = f'https://newprospect.ru{title.find("img").get("src")}'  # ссылка на изображение
        return " ".join(article_date)

def main():
    url = "https://newprospect.ru"
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()







