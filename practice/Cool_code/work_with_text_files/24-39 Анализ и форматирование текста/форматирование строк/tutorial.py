def main():
    # new len = 60
    text = "экономистов европейских но американских университетов"
    print(len(text))
    new_text = text.rjust(60, "*")
    print(new_text)
    new_text = text.ljust(60, "*")
    print(new_text)
    new_text = text.center(60, "*")
    print(new_text)
    words = text.split()



if __name__ == '__main__':
    main()
