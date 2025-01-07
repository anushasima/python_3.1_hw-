import math

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operation = input("Enter operation (it should be +, -, /, *): ")

if operation == '+':
    result = first_number + second_number
    print(f"Result is: {result}")
elif operation == '-':
    result = first_number - second_number
    print(f"Result is: {result}")
elif operation == '/' and second_number != 0:
    result = first_number / second_number
    print(f"Result is: {result}")
elif operation == '*':
    result = first_number * second_number
    print(f"Result is: {result}")
else:
    print("error")