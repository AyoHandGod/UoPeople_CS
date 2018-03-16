line1 = 'bing tiddle'
line2 = 'tiddle bang'


def print_twice(string):
    print(string)
    print(string)

def cat_twice(p1, part2):
    """
    :param p1: First string
    :param part2: Second String
    :return: None
    """
    cat = p1 + part2
    print_twice(cat)

cat_twice(line1,line2)

cat = line1 + line2
print(cat)
print(cat)

