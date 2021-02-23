# https://stepik.org/lesson/247716/step/8?unit=220169

# lst =list(map(int, input().split(" ")))
# print(lst)

start = {1, 3, 2, 4}


def digits(start, new = None):
    if len(start) == 0:
        print({})
        return
    else:
        print(start.difference({new}))
        for i in start:
            print(start.difference({i}))
        new = start.pop()
        print({new})

        digits(start)

digits(start)
