import math

def compare(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1


# Distance formula sqroot of (x2 - x1)**2 + (y2 - y1) ** 2
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    td = dx ** 2 + dy ** 2
    distance = math.sqrt(td)
    print('actual distance is', distance)
    return 0.0

# Hypotenuse says (a*2) + (b*2) = c*2
def hypotenuse(a, b):
    a2 = a * 2
    b2 = b * 2
    c2 = a2 + b2
    hypo = c2 // 2
    print("Our hypotenuse is: ", hypo)
    return hypo


def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)



def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(factorial(5))
hypotenuse(5, 8)
distance(1, 2, 3, 4)

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod


def a(x, y):
    x = x + 1
    return x * y


def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))