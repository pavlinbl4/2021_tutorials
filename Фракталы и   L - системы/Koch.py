import turtle

l = 120
ang = 60

t = turtle.Turtle()
turtle.speed(0)
width = 1200
height = 600
screen = turtle.Screen()
screen.setup(width,height, 1360, 0)

def draw_koch_segment(l,ang):
    l = l // 3
    if l > 6:
        draw_koch_segment(l,ang)
        t.lt(ang)
        draw_koch_segment(l,ang)
        t.rt(2 * ang)
        draw_koch_segment(l,ang)
        t.lt(ang)
        draw_koch_segment(l,ang)

    else:
        t.fd(l)
        t.lt(ang)
        t.fd(l)
        t.rt(2 * ang)
        t.fd(l)
        t.lt(ang)
        t.fd(l)


draw_koch_segment(l, ang)



turtle.done()