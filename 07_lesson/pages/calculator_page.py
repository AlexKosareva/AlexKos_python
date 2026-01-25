from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._result_screen = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.driver.get(" https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds):
        # Ожидаем появления поля ввода
        delay_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._delay_input)
        )
        delay_field.clear()
        delay_field.send_keys(seconds)

    def click_button(self, text):
        # Находим кнопку по тексту внутри span
        button_locator = (By.XPATH, f"//span[text()='{text}']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        ).click()

    def get_result(self):
        # Самый важный шаг: ждем появления "15" в течение 55 секунд
        # Это покрывает 45 секунд ожидания калькулятора + запас на прогрузку
        wait = WebDriverWait(self.driver, 55)
        wait.until(EC.text_to_be_present_in_element(self._result_screen, "15"))
        return self.driver.find_element(*self._result_screen).text
