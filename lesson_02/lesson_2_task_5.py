def month_to_season(month_number):
  
    if month_number in [12, 1, 2]:
        return "Зима"
    elif month_number in [3, 4, 5]:
        return "Весна"
    elif month_number in [6, 7, 8]:
        return "Лето"
    elif month_number in [9, 10, 11]:
        return "Осень"
    else:
        return "Неизвестный месяц"
    
user_input = input("Введите номер месяца (от 1 до 12): ")

try:
    month_num = int(user_input)
    season_name = month_to_season(month_num) 
    print(f"Месяц номер {month_num} относится к сезону: «{season_name}»")

except ValueError:
    print("Ошибка ввода: Пожалуйста, введите целое число от 1 до 12.")