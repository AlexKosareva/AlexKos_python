def is_year_leap(year):
    return year % 4 == 0
user_input_str = input("Введите год для проверки: ")
2
try:
    year_value = int(user_input_str)
    is_leap = is_year_leap(year_value)
    if is_leap:
        print(f"Год {year_value}: True")
    else:
        print(f"Год {year_value}: False")

except ValueError:
    print("Ошибка ввода: Пожалуйста, введите корректное целое число.")