import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage

@pytest.fixture
def driver():
    # Настройка драйвера для Chrome 2026
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    page = CalculatorPage(driver)
    
    # 1. Открыть страницу
    page.open()
    
    # 2. Ввести значение 45 в поле задержки
    page.set_delay("45")
    
    # 3. Нажать кнопки: 7, +, 8, =
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    # 4. Проверить (assert), что результат 15 появится через 45 секунд
    # Метод get_result сам дождется нужного текста
    result = page.get_result()
    assert result == "15", f"Ожидался результат 15, но получен {result}"
