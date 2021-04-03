# сортируем файлы по разрешению в директорих пользователя

from file_extension_org import create_subfol

dir_voc = {1: 'Pictures',
           2: 'Desktop',
           3: 'Google Drive',
           4: 'Public',
           5: 'Movies',
           6: 'Documents',
           7: 'Downloads'}  # словарь с директориями пользователя

print("Enter number or directory")  # выбор директории для работы
for i in dir_voc.items():
    print(f"{i[0]} - {i[1]}")
dir_key = int(input())  # пользователь выбирает диекторию - вводит ее номер
print(f"do you want to work with folder '{dir_voc[dir_key]}'?")
print('"Y" - yes/"N" - quite program')
answer = input().upper()
if answer == "Y":
    print(f'выбрана директория {dir_voc[dir_key]}')
    path = "/Users/evgeniy"
    create_subfol.finder(f'{path}/{dir_voc[dir_key]}')
elif answer == "N":
    print("GOOD BUY")
