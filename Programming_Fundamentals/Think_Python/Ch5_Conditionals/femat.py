def check_femat(a, b, c, n):
    if (a ** n) + (b ** n) == (c ** n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")


def gather_fem():
    a = int(input("Provide A\n"))
    b = input("Provide B\n")
    c = input("Provide C\n")
    n = input("Provide N\n")
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    check_femat(a, b, c, n)


gather_fem()
gather_fem()