import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и закрытия драйвера Chrome.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.epic("Автоматизация калькулятора")
@allure.feature("Медленный калькулятор")
@allure.story("Операции сложения с задержкой")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест медленного сложения (7 + 8)")
@allure.description(
    "Проверка, что калькулятор корректно выводит 15 после задержки 45 сек."
)
def test_slow_calculator(driver):
    """
    Тестовый сценарий для проверки сложения с ожиданием результата.
    """
    page = CalculatorPage(driver)

    page.open()
    page.set_delay(45)

    with allure.step("Ввести выражение: 7 + 8"):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    result = page.get_result()

    with allure.step("Проверить, что итоговый результат равен 15"):
        assert result == "15", f"Ожидался результат 15, но получен {result}"
