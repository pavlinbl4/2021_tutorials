def main():
    text = "С 1 июля авиакомпания Turkish"
    # 50 длина новой строки после выравнивания пробелами
    probel_to_add = 50 - len(text)  # количество пробелов, которое нужно добавить
    words = text.split() # преобразую строку в список
    count = 0
    while count < probel_to_add:
        for i in range(len(words) - 1, 0, -1):
            if count < probel_to_add:
                words[i] = " " + words[i]
                count += 1
            else:
                break

    new_text = " ".join(words)
    # new_text = new_text.replace("*"," ")
    print(new_text)
    print(len(new_text))



if __name__ == '__main__':
    main()