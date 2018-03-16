def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


print(first("word"))
print(middle("Word"))
print(middle("a"))
print(middle("ab"))


def is_palindrome(word):
    if len(word) <=1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


print(is_palindrome("WordroW"))


def is_power(a, b):
    c = a / b
    if c == 0 or c < 1:
        return False
    if c == b:
        return True
    return is_power(c, b)


print(is_power(80, 2))

def GCD(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        print("r currently is: ", r)
        return GCD(b, r)


print(GCD(40, 20))