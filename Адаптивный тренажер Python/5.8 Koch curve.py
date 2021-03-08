# https://stepik.org/lesson/21972/step/1?adaptive=true&unit=5232

import turtle
turtle.speed(1)
t = turtle.Pen()
len = 40
n = 2

def main_way(len):
    if len > 1:
        t.fd(len/2)
        t.lt(60)
        t.fd(len/2)
        t.lt(-120)
        t.fd(len/2)
        t.lt(60)
        t.fd(len/2)



main_way(len)

def main(len):
    main_way(len)
    t.lt(60)
    main_way(len)
    t.lt(-120)
    main_way(len)
    t.lt(60)
    main_way(len)
#
#
#     main()
#     t.lt(60)
#     main()
#     t.lt(-120)
#     main()
#     t.lt(60)
#     main()










turtle.mainloop()