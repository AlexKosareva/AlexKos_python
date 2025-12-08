import math

def square(a):
    area = a*a

    if not isinstance(a, int):
        return math.ceil(area)
    else:
        return area

user_input_str = input("Введите длину стороны квадрата: ")

try:
    a_value = float(user_input_str)
    calculated_area = square(a_value)
    print(f"Площадь квадрата: {calculated_area}")

except ValueError:
    print("Пожалуйста, введите корректное число.")

