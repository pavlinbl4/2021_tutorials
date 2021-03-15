import pyperclip
lesson = 'seq'   # func
number = 33
text = ''

for i in range(1,number + 1):
    text += f"def {lesson}{i}():\n    pass\n\n\n{lesson}{i}()\n{lesson}{i}()\n{lesson}{i}()\n\n\n"
    # print(f"def {lesson}{i}():\n    pass\n\n\n{lesson}{i}()\n{lesson}{i}()\n{lesson}{i}()\n\n\n")
    pyperclip.copy(text)
    print(text)
