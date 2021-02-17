import openpyxl
import datetime
from openpyxl import load_workbook

book = openpyxl.Workbook() # создание новой таблицы с перезаписью старой
sheet = book.active


book.title = "Kommersant"
# sheet.cell(row =1,column=2).value = "Дата"
# sheet.cell(row =3,column=1).value = datetime.datetime.now()

# sheet.cell(row =2,column=1).value = "photo id"
# sheet.cell(row =3,column=2).value = "7777"

book.save("/Volumes/big4photo/Documents/Kommersant/publications.xlsx")
book.close()