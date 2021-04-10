
try:
    a = float(input())
    b = float(input())
    print(a / b)
except ZeroDivisionError:
    print("Please don't divide by zero")
except ValueError:
    print("Please input real numb")
finally:
    print("end of the programm")
