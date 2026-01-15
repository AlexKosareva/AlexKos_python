from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера (в 2026 году Selenium сам управляет драйверами)
driver = webdriver.Chrome()

try:
    # 1. Перейти на страницу (обязательно с http://)
    driver.get("http://uitestingplayground.com/ajax")

    # 2. Нажать на синюю кнопку (ID: ajaxButton)
    driver.find_element(By.ID, "ajaxButton").click()

    # 3. Получить текст из зеленой плашки
    # Используем WebDriverWait вместо sleep(). Ждем появления элемента до 20 секунд.
    waiter = WebDriverWait(driver, 20)
    
    # Ищем плашку по CSS-классу bg-success (зеленый фон)
    content = waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )

    # 4. Вывести текст в консоль
    print(content.text)

finally:
    # Закрыть браузер
    driver.quit()
