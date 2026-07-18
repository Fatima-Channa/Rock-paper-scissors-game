import math as m

count = True

while count:
    user = input("Choose an operation to be performed (+, -, *, /, sin, cos) or type 'end' to exit: ").casefold()

    if user == "end":
        print("Calculator shutting down!")
        break

    if user == "+" or user == "-" or user == "*" or user == "/":
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

    elif user == "sin" or user == "cos":
        input_value = float(input("Enter the value: "))
        unit = input("Is the value in degrees or radians? (degree/radians): ").casefold()

        if unit == "degree":
            angle = m.radians(input_value)
        elif unit == "radians":
            angle = input_value
        else:
            print("Invalid unit. Please enter degree or radians.")
            continue

    else:
        print("Invalid operation. Please try again.")
        continue

    if user == "+":
        result = n1 + n2
        print("The result is:", result)
    elif user == "-":
        result = n1 - n2
        print("The result is:", result)
    elif user == "*":
        result = n1 * n2
        print("The result is:", result)
    elif user == "/":
        if n2 != 0:
            result = n1 / n2
            print("The result is:", result)
        else:
            print("Can't divide by zero.")

    elif user == "sin":
        result = m.sin(angle)
        print("The sin of", input_value, "is:", result)

    elif user == "cos":
        result = m.cos(angle)
        print("The cos of", input_value, "is:", result)