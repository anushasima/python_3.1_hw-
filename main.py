import operator


def calculator():
    allowed_operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    print("Калькулятор підтримує операції: +, -, *, /")

    while True:
        try:
            my_value = input("Введіть вираз у форматі: число оператор число (наприклад, 2 + 3): ").strip()
            tokens = my_value.split()

            if len(tokens) != 3:
                raise ValueError("Введіть вираз у форматі: число оператор число.")

            num1, operator_symbol, num2 = tokens
            num1 = float(num1)
            num2 = float(num2)

            if operator_symbol not in allowed_operators:
                raise ValueError(f"Оператор '{operator_symbol}' не підтримується.")

            result = allowed_operators[operator_symbol](num1, num2)
            print(f"Результат: {result}")

        except Exception as e:
            print(f"Помилка: {e} \nСпробуйте ще раз.")
            continue

        continue_calculating = input("Бажаєте продовжити? (y or yes для продовження): ").strip().lower()
        if continue_calculating not in ('y', 'yes'):
            print("Завершено.")
            break


calculator()