def is_triangle(side1, side2, side3):
    if side1 > side2 and side1 > side3:
        if side2 + side3 >= side1:
            print("Yes")
        else:
            print("No")
    elif side2 > side3:
        if side1 + side3 >= side2:
            print("Yes")
        else:
            print("No")
    elif side1 + side2 >= side3:
        print("Yes")
    else:
        print("No")


def biggest(side1, side2, side3):
    if side1 > side2 and side1 > side3:
        return side1
    elif side2 > side3:
        return side2
    else:
        return side3


def take_angles():
    side1 = input("Side 1 value: ")
    side2 = input("Side 2 value: ")
    side3 = input("Side 3 value: ")
    side1 = int(side1)
    side2 = int(side2)
    side3 = int(side3)
    return is_triangle(side1, side2, side3)


take_angles()