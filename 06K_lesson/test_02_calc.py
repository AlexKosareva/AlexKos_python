import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_slow_calculator():
    # Настройка драйвера для Google Chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # 1. Открыть страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. В поле ввода по локатору #delay ввести значение 45
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # 3. Нажать на кнопки: 7, +, 8, =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # 4. Проверить, что в окне отобразится результат 15 через 45 секунд
    # Используем WebDriverWait с запасом (например, 50 секунд), так как sleep() запрещен
    waiter = WebDriverWait(driver, 50)
    
    # Ждем, пока в элементе с классом 'screen' (окно калькулятора) появится текст '15'
    waiter.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    # Итоговая проверка
    result_text = driver.find_element(By.CLASS_NAME, "screen").text
    assert result_text == "15"

    driver.quit()
