import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """
    Класс для управления страницей оформления заказа.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу оформления заказа.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self._first_name = (By.ID, "first-name")
        self._last_name = (By.ID, "last-name")
        self._zip_code = (By.ID, "postal-code")
        self._continue_btn = (By.ID, "continue")
        self._total_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить форму заказа: {first} {last}, индекс: {zip_code}")
    def fill_form(self, first: str, last: str, zip_code: str) -> None:
        """
        Заполняет персональные данные покупателя и переходит к следующему шагу.

        :param first: Имя покупателя (строка).
        :param last: Фамилия покупателя (строка).
        :param zip_code: Почтовый индекс (строка).
        :return: None
        """
        self.driver.find_element(*self._first_name).send_keys(first)
        self.driver.find_element(*self._last_name).send_keys(last)
        self.driver.find_element(*self._zip_code).send_keys(zip_code)
        self.driver.find_element(*self._continue_btn).click()

    @allure.step("Получить итоговую сумму заказа")
    def get_total(self) -> str:
        """
        Считывает итоговую стоимость из блока информации о заказе.

        :return: Итоговая сумма в виде строки (например, '$58.29').
        """
        total_text = self.driver.find_element(*self._total_label).text
        # Извлекаем только сумму, убирая текст "Total: "
        result = total_text.split("Total: ")[1]
        return result
