# Our compare function. Use try/except to validate that numbers are provided
def compare(a, b):
    try:
        a = float(a)
    except ValueError:
        print("This function requires two numbers to work")
        print("The first item is not a valid number.")
    try:
        b = float(b)
    except ValueError:
        print("This function requires two numbers to work")
        print("The second items is not a valid number.")
    else:
        if a > b:
            return 1
        elif a == b:
            return 0
        else:
            return -1

# Our test cases
print(compare(5,2))
print(compare(2,5))
print(compare(3,3))

# Gather users input
n1 = input("Provide first number: ")
n2 = input("Provide second number: ")

# use function on user inputs
print(compare(n1,n2))