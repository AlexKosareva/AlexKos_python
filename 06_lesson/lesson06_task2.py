from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

try:
    # 1. Перейти на сайт
    driver.get("http://uitestingplayground.com/textinput")

    # 2. Указать в поле ввода текст SkyPro
    # Находим поле по ID 'newButtonName'
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    # 3. Нажать на синюю кнопку
    # Находим кнопку по ID 'updatingButton'
    updating_button = driver.find_element(By.ID, "updatingButton")
    updating_button.click()

    # 4. Получить текст кнопки и вывести в консоль
    # После клика текст кнопки должен измениться на "SkyPro"
    print(updating_button.text)

finally:
    # Закрыть браузер
    driver.quit()
