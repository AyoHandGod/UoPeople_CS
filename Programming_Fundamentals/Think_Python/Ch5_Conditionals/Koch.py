import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


def koch(t, length):
    if length < 3:
        t.fd(length)
        return
    else:
        kl = length/3
        koch(t, kl)
        t.lt(60)
        koch(t, kl)
        t.rt(120)
        koch(t, kl)
        t.lt(60)
        koch(t, kl)



def snowflake(t, n):
    for i in range(3):
        koch(t, n)
        t.rt(120)

paul = turtle.Turtle()

koch(paul, 50)
snowflake(paul, 400)

turtle.mainloop()