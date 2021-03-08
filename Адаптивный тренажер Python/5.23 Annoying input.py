# https://stepik.org/lesson/26124/step/1?adaptive=true&unit=8110

def get_int(start_message, error_message, end_message):
    print(start_message)
    while True:
        x = input()
        if len(x) >1 and x[1:].isdigit() == True or len(x) == 1 and x.isdigit() == True:
            print(end_message)
            return int(x)
        print(error_message)













x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')