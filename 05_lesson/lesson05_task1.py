from selenium import webdriver
from selenium.webdriver.common.by import By

# В 2026 году Selenium сам находит драйвер для Chrome 144
driver = webdriver.Chrome()

try:
    # 1. Перейти на страницу
    driver.get("uitestingplayground.com")
    
    # 2. Кликнуть на синюю кнопку
    # Мы используем CSS-селектор .btn-primary, так как ID там динамический
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    blue_button.click()
    
    # 3. Обработка окна Alert
    alert = driver.switch_to.alert
    print(f"Окно открыто: {alert.text}")
    alert.accept()

finally:
    driver.quit()