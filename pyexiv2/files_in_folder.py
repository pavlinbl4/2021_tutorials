import os

path = '/Users/evgeniy/Downloads/jpg'
items = os.listdir(path)
file_list = []
for item in items:
    fullname = os.path.join(path, item)
    if os.path.isfile(fullname) and item.endswith('jpg'):
        file_list.append(fullname)
print(file_list)