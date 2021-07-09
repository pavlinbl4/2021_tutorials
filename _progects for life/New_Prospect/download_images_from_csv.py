"""
скрипт должен считывать информацию из CSV  файла
и скачивать изображения за указанный месяц
"""
import csv
import requests
import os

def image_downloader(csv_file_path,month,month_number):
    os.makedirs(f"/Volumes/big4photo/Documents/NewProspect/2021_{month_number}", exist_ok=True)
    with open(csv_file_path,'r') as input_file:
        reader = csv.reader(input_file)
        for row in reader:
            if month in row[0]:
                image_link = row[2]
                r = requests.get(image_link, stream=True)
                with open(
                        f"/Volumes/big4photo/Documents/NewProspect/2021_{month_number}/{row[0]}__{row[1]}.JPG",
                        "bw") as f:
                    for chunk in r.iter_content(9000):
                        f.write(chunk)

def date_convert(month_number): # функция преоразует введенный номер месяца в его название

    voc = {1: 'января',
           2: 'февраля',
           3: 'марта',
           4: 'апреля',
           5: 'мая',
           6: 'июня',
           7: 'июля',
           8: 'августа',
           10: 'октября',
           11: 'ноября',
           12: 'декабря'}
    month_name = voc[month_number]
    return month_name



print("ENTER NUMBER OF MONTH\n")
month_number = int(input())
date_convert(month_number)

month = date_convert(month_number)
csv_file_path = "/Users/evgeniy/PycharmProjects/2021_tutorials/_progects for life/New_Prospect/NP.csv"
image_downloader(csv_file_path,month,month_number)