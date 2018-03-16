import do_twice

length = 21
height = 11

n = "+ - - - - + - - - - +"
g = "/         /         /"

def grid(n, g):
    print(n * 2)
    do_twice.do_better(do_twice.print_twice,g * 2)
    print(n * 2)
    do_twice.do_better(do_twice.print_twice,g * 2)
    print(n * 2)

grid(n, g)
