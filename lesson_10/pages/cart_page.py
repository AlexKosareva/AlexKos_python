import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """
    Класс для управления страницей корзины интернет-магазина.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу корзины.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self._checkout_btn = (By.ID, "checkout")

    @allure.step("Нажать кнопку 'Checkout' в корзине")
    def checkout(self) -> None:
        """
        Выполняет переход к этапу оформления заказа.

        :return: None
        """
        self.driver.find_element(*self._checkout_btn).click()
