# https://stepik.org/lesson/21208/step/2?adaptive=true&unit=5094

import  math

def f(x):
    if x <= -2:
        return 1 - (x +2)**2
    if -2 < x <= 2:
        return -x/2
    if x > 2:
        return (x -2)**2 + 1

print(f(4.5))