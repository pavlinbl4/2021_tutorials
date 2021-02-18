# из отчета TASS извлекает код фото и сумму
import openpyxl

wb = openpyxl.load_workbook('/Users/evgeniy/Downloads/Павленко.xlsx')
sheet = wb.active
photos = {}
x = 7
id = (sheet.cell(row=x, column=4)).value
money = (sheet.cell(row=x, column=6)).value
while id != None:
    print(photos.setdefault(id,[]))
    photos[id].append(round(money,3))
    x += 1
    id = (sheet.cell(row=x, column=4)).value
    money = (sheet.cell(row=x, column=6)).value
for i in photos:
    print(f"{i} - {photos[i]}")
