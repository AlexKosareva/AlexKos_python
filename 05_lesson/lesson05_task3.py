from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Открыть браузер Firefox
# Selenium автоматически скачает geckodriver, если его нет
driver = webdriver.Firefox()

try:
    # 2. Перейти на страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Находим поле ввода (оно там одно, типа number)
    input_field = driver.find_element(By.TAG_NAME, "input")

    # 3. Ввести в поле текст Sky (в поле типа number текст не введется, 
    # но по заданию мы выполняем команду)
    input_field.send_keys("Sky")

    # 4. Очистить это поле
    input_field.clear()

    # 5. Ввести в поле текст Pro
    input_field.send_keys("Pro")

    print("Задание 3 выполнено успешно!")

finally:
    # 6. Закрыть браузер
    driver.quit()