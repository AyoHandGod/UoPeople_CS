def new_line():
    print()


# uses new_lines function 3x to print 3 lines
def three_lines():
    new_line()
    new_line()
    new_line()

# uses three_lines function 3x to print 9 lines
def nine_lines():
    three_lines()
    three_lines()
    three_lines()


# uses nine_lines 2x, three_lines 2x, and new_line 1 time for a total
# of 25 lines
def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()


nine_lines()
print("printed 9 lines, now printing 25....")
clear_screen()
