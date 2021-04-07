import pyexiv2

way = '/Users/evgeniy/Downloads/jpg/KSP_015709_00125_1h.jpg'
img = pyexiv2.Image(way)
data = img.read_iptc()
for i in data.items():
    print(i)
img.close()