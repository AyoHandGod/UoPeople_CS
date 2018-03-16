import math

def mysqrt(a):
    x = 1
    epsilon = 0.000000001
    while True:
        print(x)
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y


def test_square_root():
    mysqs = []
    matsqs = []
    for i in range(1, 9):
        mysqs.append(mysqrt(i))
        matsqs.append(math.sqrt(i))
    for i in mysqs:
        print("{: >20} {: >20} {: >20}".format(*i))

test_square_root()