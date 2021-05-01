# https://stepik.org/lesson/21972/step/1?adaptive=true&unit=5232

import turtle

turtle.speed(0)
t = turtle.Pen()
ln = 200
n = 3



def main_way(ln):
    if ln > 200:
        ln3 = ln // 3
        main_way(ln3)
        t.lt(60)
        main_way(ln3)
        t.rt(120)
        main_way(ln3)
        t.lt(60)
        main_way(ln3)
    else:

        t.fd(ln)
        t.lt(60)
        t.fd(ln)
        t.rt(120)
        t.fd(ln)
        t.lt(60)
        t.fd(ln)


main_way(ln)

turtle.mainloop()
