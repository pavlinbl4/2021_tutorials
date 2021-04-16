# переименовываю фото солгасно данным из IPTC
import pyexiv2
import os

path = '/Users/evgeniy/Downloads/jpg/KSP_016535_00025_1h.jpg'
img = pyexiv2.Image(path)
data = img.read_iptc()

ymd = data['Iptc.Application2.DigitizationDate'].replace("-","")
time = data['Iptc.Application2.DigitizationTime'].replace(":","")[:-5]

new_name = f'{ymd}_PEV_{time}.JPG'
new_way = f'{os.path.split(path)[0]}/{new_name}'
os.rename(path,new_way)
img.close()


path = os.path.split(path)[0]   # check result
items = os.listdir(path)
extensions = ('jpg', 'jpeg','JPG') # кортеж с допустимыми разрешениями файлов
for item in items:
    fullname = os.path.join(path, item)
    # print(item)
    if os.path.isfile(fullname) and item.endswith(extensions):
        print(item)