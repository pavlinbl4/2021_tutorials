import os
import pyexiv2

path = '/Users/evgeniy/Downloads/jpg'
items = os.listdir(path)
file_list = []
for item in items:
    fullname = os.path.join(path, item)
    if os.path.isfile(fullname) and item.endswith('jpg'):
        file_list.append(fullname)


for i in file_list:
    path = i
    img = pyexiv2.Image(path)
    data_old = img.read_iptc()
    caption = data_old['Iptc.Application2.Caption']
    caption = caption.replace("Kommersant Photo/Yevgeny Pavlenko \r\n#RU ", "")
    caption = caption.replace(" Фото: Евгений Павленко/Коммерсантъ", "")
    dict1 = {'Iptc.Application2.Byline': ['Pavlenko Evgeniy'],
             'Iptc.Application2.Copyright': '(c) Pavlenko Evgeniy',
             'Iptc.Application2.Credit': 'Pavlenko Evgeniy',
             'Iptc.Application2.Caption': caption
             }
    data = img.modify_iptc(dict1)
    img.close()


for i in file_list:
    path = i
    img = pyexiv2.Image(path)
    data_new = img.read_iptc()
    for i in data_new.items():
        print(i)
    print("-" * 50)