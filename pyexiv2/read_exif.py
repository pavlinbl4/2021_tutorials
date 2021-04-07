import pyexiv2


way_to_img = '/Users/evgeniy/Downloads/jpg/KSP_015709_00125_1h.jpg'
img = pyexiv2.Image(way_to_img)
exif_data = img.read_exif()
for i in exif_data.items():
    print(i)
# print(exif_data['Exif.Image.Software'])
# print(exif_data['Exif.Image.DateTime'])
# print(exif_data['Exif.Photo.DateTimeDigitized'])