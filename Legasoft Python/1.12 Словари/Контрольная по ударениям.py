voc = {}
for i in range(int(input())):
    text = input()
    voc.setdefault(text.lower(),[]).append(text)
text = input().split()
words = len(text)
for i in text:
    if i.lower() not in voc:
        words -= 1
    elif i.islower() and i.isupper():
        words += 1
    else:
        if i in voc[i.lower()]:
            words -= 1
print(words)
