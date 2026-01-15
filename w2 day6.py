#i can combine functions and logic to build a complete script

def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Invalid operation"
    
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# gather inputs
if operation == "/" and number2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    result = calculate(number1, number2, operation)
    print("The result is:", result)