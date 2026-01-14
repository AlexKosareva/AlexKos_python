from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Открыть браузер Google Chrome
# Selenium 4 автоматически скачает нужный драйвер для версии 144
driver = webdriver.Chrome()

try:
    # 2. Перейти на страницу
    # Обязательно указываем полный путь с http://
    driver.get("http://uitestingplayground.com/classattr")

    # 3. Кликнуть на синюю кнопку
    # Ищем по CSS-классу .btn-primary. 
    # Так как ID меняется, поиск по классу — самый надежный способ.
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    blue_button.click()

    # После клика появляется модальное окно (Alert), его нужно закрыть
    alert = driver.switch_to.alert
    print(f"Текст уведомления: {alert.text}")
    alert.accept()

finally:
    # Закрыть браузер
    driver.quit()
