from selenium import webdriver
from selenium.webdriver.common.by import By

# В 2026 году Selenium сам управляет драйверами, доп. настройки не нужны
driver = webdriver.Chrome()

try:
    # 1. Перейти на страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # 2. Кликнуть на синюю кнопку
    # Так как ID динамический, ищем кнопку по тексту "Button with Dynamic ID"
    # или по синему классу btn-primary
    blue_button = driver.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]')
    blue_button.click()

    print("Клик выполнен успешно!")

finally:
    # 3. Закрыть браузер
    driver.quit()