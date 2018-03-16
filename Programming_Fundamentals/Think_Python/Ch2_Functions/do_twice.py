from spaces import right_justify as rj

def do_twice(func):
    func()
    func()

def spam():
    print('spammage')

# do_twice(spam)

def do_better(func, arg):
    func(arg)
    func(arg)

# do_better(rj,'Dante')

def print_twice(bruce):
    print(bruce)
    print(bruce)

# do_better(print_twice, 'spam')

def do_best(func, arg):
    do_better(func, arg)
    do_better(func, arg)

# do_best(print_twice, 'spam')

