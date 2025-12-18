import math

def calculate_factorial():
    try:
        user_input = input("Введите положительное целое число: ")
        number = int(user_input)

        if number < 0:
            print("Ошибка: необходимо ввести положительное число.")
            return

        result = math.factorial(number)
        print(f"Факториал числа {number} равен {result}")

    except ValueError:
        print("Ошибка: введено нечисловое значение.")

calculate_factorial()
