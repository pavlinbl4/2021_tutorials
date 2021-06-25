"""
пропорционаьное изменение  размера снимка
"""
from PIL import Image

image = Image.open('/Users/evgeniy/Downloads/KSP_017079_00009_1m.jpg')
image.thumbnail((200, 200))
image.save('/Users/evgeniy/Downloads/KSP_017079_00009_1m.jpg')

