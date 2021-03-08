# https://stepik.org/lesson/21210/step/1?adaptive=true&unit=5096

text = input().lower().split()
only_one = set(text)
print(only_one)

for word in only_one:
    print(f"{word} {text.count(word)}")


[print( f(x) for  int(input()) in range(int(input()))]