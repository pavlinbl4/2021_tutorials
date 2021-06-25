from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

ws.column_dimensions['A'].width = 40  # задаю шрину колонки
ws.row_dimensions['1'].height = 150  # задаю выссоту столбца

img = Image('/Users/evgeniy/Downloads/KSP_017175_00006_1m.jpg')

resize_height = img.height // 2  # уменьшая рарешение в два раза
resize_width = img.width // 2  # уменьшая рарешение в два раза

img.width = resize_width  # устанавливаю размер превью
img.height = resize_height  # устанавливаю размер превью

ws.add_image(img, 'A1')  # записываю снимок в заданную ячейку

wb.save('logo.xlsx')
