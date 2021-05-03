n = int(input())
all_numbers = {x for x in range(1, n + 1)}

while True:
    data = input()
    if data == "HELP":
        print(*all_numbers)
        break
    else:
        numbers = set(map(int, data.split()))
        answer = input()
        if answer == "NO":
            all_numbers.difference_update(numbers)
        elif answer == "YES":
            all_numbers.intersection_update(numbers)
