import pyexiv2

way = '/Users/evgeniy/Downloads/jpg/KSP_015709_00125_1h.jpg'
img = pyexiv2.Image(way)
# img.clear_iptc()
# img.clear_exif()
# img.clear_xmp()
img.clear_icc()
img.close()