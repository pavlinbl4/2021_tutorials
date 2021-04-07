# чтение IPTC данных
import pyexiv2


img = pyexiv2.Image('/Users/evgeniy/Downloads/jpg/KSP_016535_00025_1h.jpg')
data = img.read_iptc()
for i in data.items():
    print(i)
# print(data['Iptc.Application2.Keywords'])
# print(data['Iptc.Application2.Caption'])
img.close()