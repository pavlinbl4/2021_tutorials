"""
программа создает сабфолдеры по расширениям файлов
в заданной директории и переносит их туда
"""
import os
import shutil


def finder(path):
    names = os.listdir(path)
    for name in names:
        fullname = os.path.join(path, name)
        flag = True
        if os.path.isfile(fullname) and name[0] != ".":
            try:
                os.makedirs(f'{path}/{name.split(".")[-1]}', exist_ok=True)  # создаю папку по имени расширения файла
                shutil.move(fullname,
                            f'{path}/{name.split(".")[-1]}/{name}')  # команда переносит файл в новую директорию
                print(f'new folder created - {name.split(".")[-1]}')
                flag = False
            except FileExistsError:
                print(f'problem with file {name}')  # при проблемах с файлами, пропустить их
            finally:
                continue
    print('Not need in optimization' * flag)


finder("/Users/evgeniy/Public")
# finder(path)
