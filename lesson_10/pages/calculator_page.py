import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Класс для управления страницей медленного калькулятора.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу калькулятора.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._result_screen = (By.CSS_SELECTOR, ".screen")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """
        Открывает страницу медленного калькулятора в браузере.

        :return: None
        """
        # Перенос строки для соответствия PEP8 (длина строки)
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    @allure.step("Установить задержку в {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает значение задержки выполнения операций.

        :param seconds: Время задержки в секундах (целое число).
        :return: None
        """
        delay_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._delay_input)
        )
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    @allure.step("Нажать на кнопку '{text}'")
    def click_button(self, text: str) -> None:
        """
        Находит и нажимает на кнопку калькулятора с указанным текстом.

        :param text: Текст на кнопке (например, '7', '+', '=').
        :return: None
        """
        button_locator = (By.XPATH, f"//span[text()='{text}']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        ).click()

    @allure.step("Получить результат вычисления")
    def get_result(self) -> str:
        """
        Ожидает завершения вычисления и возвращает итоговое значение с экрана.

        :return: Текст (результат), отображаемый на экране калькулятора.
        """
        # Ожидание 55 секунд для учета максимальной задержки калькулятора
        wait = WebDriverWait(self.driver, 55)
        wait.until(EC.text_to_be_present_in_element(self._result_screen, "15"))
        return self.driver.find_element(*self._result_screen).text
