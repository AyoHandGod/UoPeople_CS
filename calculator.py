# Takes in our first number
number1 = input("Provide first number please: \n")
while True:
    try:
        number1 = int(number1)
        break
    except:
        number1 = input("Please provide a number: \n")

# Takes in the number for the operation we wish to perform
print("Which operation would you like to perform?")
operation = input("Enter 1 to Add, 2 to subtract, 3 to multiply, 4 to divide: \n")
while True:
    try:
        operation = int(operation)
    except:
        operation = input("Enter 1 to Add, 2 to subtract, 3 to multiply, 4 to divide: \n")
    finally:
        if operation == 1 or operation == 2 or operation == 3 or operation == 4:
            break
        else:
            operation = input("Enter 1 to Add, 2 to subtract, 3 to multiply, 4 to divide: \n")

# Takes in our second number
number2 = input("Provider second number please: \n")
while True:
    try:
        number2 = int(number2)
        break
    except:
        number2 = input("Please provide a number: \n")

# Perform our mathematical equation depending on the operation selected
if operation == 1:
    total = number1 + number2
elif operation == 2:
    total = number1 - number2
elif operation == 3:
    total = number1 * number2
else:
    total = number1 / number2

# Print a space and then the total
print("\n")
print(total)
