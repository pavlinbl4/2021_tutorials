# This Python file uses the following encoding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version
from mail_token import user, password

server = 'smtp.mail.ru'
user = user
password = password

subject_dict = { 1 : "для Романова", 2 : "для Кустовой", 3 : "для Кауровой", 4 : "для Груздевой", 5 : "для Семенова", 6 : "для Соболева", 7 :"для Дьяченко",8 :"для Лемешевой"}
recipients_dict ={1:'romanov@spb.kommersant.ru',
                  2:'kustova@spb.kommersant.ru',
                  3:"kaurova@spb.kommersant.ru",
                  4:"gruzdeva@spb.kommersant.ru",
                  5:"agenty@spb.kommersant.ru",
                  6:"sobolev@spb.kommersant.ru",
                  7:"dyachenko@spb.kommersant.ru",
                  8:"lemesheva@spb.kommersant.ru"}

print("Введи ID фотографии ")
photo_id = str()

n = input()
if n[:3] != "KSP":
    print("NOT VALID ID NUMBER START AGAIN")
else:

    while n != "":
        photo_id = photo_id +'\n'+ n
        n = input()



    print("""выбери заказчика фото
          1 : для Романова 
          2 : для Кустовой
          3 : для Кауровой
          4 : для Груздевой
          5 : для Семенова
          6 : для Соболева
          7 : для Дьяченко
          8 : для Лемешевой""")
    customer = int(input())


    recipients = ['techdep@spb.kommersant.ru','almargolin@yandex.ru', 'pavlenko-e@mail.ru',recipients_dict[customer]]
    # recipients = ['pavlenko-e@mail.ru']
    sender = 'pelikan_600@mail.ru'
    subject = subject_dict[customer]
    text = photo_id
    # html = '<html><head></head><body><p>' + text + '</p></body></html>'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Evgeniy Pavlenko <' + sender + '>'


    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = 'pavlenko.evgeniy@gmail.com'
    msg['Return-Path'] = 'pavlenko.evgeniy@gmail.com'
    msg['X-Mailer'] = 'Python/' + (python_version())

    part_text = MIMEText(text, 'plain')
    # part_html = MIMEText(html, 'html')

    msg.attach(part_text)
    # msg.attach(part_html)

    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()