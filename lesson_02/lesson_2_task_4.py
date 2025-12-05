def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

user_input_str = input("Введите целое число n для FizzBuzz: ")
n_value = int(user_input_str)
print(f"Запускаем FizzBuzz до числа {n_value}")
fizz_buzz(n_value)