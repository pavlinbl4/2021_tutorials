import pyexiv2

path = '/Users/evgeniy/Downloads/jpg/KSP_016878_00248_1h.jpg'
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
img.modify_iptc(dict1)
img.close()


# img = pyexiv2.Image('/Users/evgeniy/Downloads/jpg/KSP_015709_00125_1h.jpg')  # check rezult
# data_new = img.read_iptc()
# for i in data_new.items():
#     print(i)
# img.close()
