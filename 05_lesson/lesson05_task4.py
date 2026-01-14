from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Открываем браузер Firefox
driver = webdriver.Firefox()

try:
    # 2. Переходим на страницу авторизации
    driver.get("http://the-internet.herokuapp.com/login")

    # 3. В поле username вводим tomsmith
    # Находим элемент по его ID
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("tomsmith")

    # 4. В поле password вводим SuperSecretPassword!
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword!")

    # 5. Нажимаем кнопку Login
    # Кнопка имеет тип submit, ищем её через CSS-селектор
    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()

    # 6. Выводим текст с зеленой плашки (flash message) в консоль
    # Сообщение об успехе имеет ID 'flash'
    flash_message = driver.find_element(By.ID, "flash")
    print(f"Текст уведомления: {flash_message.text}")

finally:
    # 7. Закрываем браузер
    driver.quit()
