import math


# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))
# operation = input("Enter operation (it should be +, -, /, *): ")
#
# if operation == '+':
#     result = first_number + second_number
#     print(f"Result is: {result}")
#
# elif operation == '-':
#     result = first_number - second_number
#     print(f"Result is: {result}")
# elif operation == '/' and second_number != 0:
#     result = first_number / second_number
#     print(f"Result is: {result}")
# elif operation == '*':
#     result = first_number * second_number
#     print(f"Result is: {result}")

# else:
#     print("error")


def calculator():
    while True:
        try:
            operation = input("Введіть якийсь мат вираз (наприклад 2+3): ")
            result = eval(operation)
            print(f"Результат: {result}")
        except operation as e:
            print(f"Помилка: {e}. Спробуйте ще раз.")
        continue_calculating = input("Бажаєте продовжити? (y для продовження, n - для завершення): ").strip().lower()
        if continue_calculating not in ('y', 'yes'):
            print("завершено")
            break

calculator()