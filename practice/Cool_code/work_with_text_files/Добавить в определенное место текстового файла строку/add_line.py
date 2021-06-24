"""Имеется текстовый файл.
Добавить в него строку из двенадцати черточек (————),
разместив ее:
• после пятой строки;
 """

with open('test_txt.txt','r') as poem:
    lines_befor_5 = poem.readlines()[:5] # срез первых пяти строк
    lines_afret_5 = poem.readlines()[5:]
    print(lines_afret_5)


