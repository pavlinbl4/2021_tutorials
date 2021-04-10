import turtle

l = 120
ang = 60

t = turtle.Turtle()
turtle.speed(0)
width = 1200
height = 600
screen = turtle.Screen()
screen.setup(width, height, 1360, 0)
count = 0

n = 2
if n == 0:
    print()
else:

    def draw_koch_segment(l, ang, n):
        l = l // 3
        n -= 1
        if n > 0:
            draw_koch_segment(l, ang, n)
            t.lt(ang)
            draw_koch_segment(l, ang, n)
            t.rt(2 * ang)
            draw_koch_segment(l, ang, n)
            t.lt(ang)
            draw_koch_segment(l, ang, n)



        else:
            # count += 1
            t.fd(l)
            t.lt(ang)
            print('turn 60')
            t.fd(l)
            t.rt(2 * ang)
            print('turn -120')
            t.fd(l)
            t.lt(ang)
            print('turn 60')
            t.fd(l)
            print("*" * 50)


    draw_koch_segment(l, ang, n)
# print(count)

turtle.done()
