def test_user(users, name):
    print(f'users = {users},name = {name} ')
    if name in users:
        count = 1
        new_name = f'{name}{count}'
        while new_name in users:
            count += 1
            new_name = f'{name}{count}'
        users.setdefault(new_name)
        return new_name
    users.setdefault(name)
    return "OK"


n = int(input())
users = {}
for x in range(n):
    name = input()
    print(test_user(users, name))
