import turtle
import math
bob = turtle.Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def square(t, l):
    try:
        type(t) == turtle.Turtle()
    except:
        print("Wrong type")
    finally:
        for x in range(4):
            t.color("purple")
            t.begin_fill()
            t.fd(l)
            t.lt(90)
            t.end_fill()


def polygon(t, l, n):
    try:
        type(t) == turtle.Turtle()
    except:
        print("Wrong type")
    finally:
        t.color("green")
        angle = 360.0/n
        polyline(t, n, l, angle)


def circle(t, r):
    """
    :param t: turtle object
    :param r: int value for radius
    :return: turtle drawn circle
    """
    # Calculate the circumference
    arc(t, r, 360)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle /360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    polyline(t, n, step_length, step_angle)

#square(bob, 100)
polygon(bob, 100, 3)
# circle(bob, 30)
# arc(bob, 50, 180)
arc(bob, 50, 180)
turtle.mainloop()
