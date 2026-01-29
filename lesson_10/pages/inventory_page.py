import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """
    Класс для работы со страницей каталога товаров (Inventory).
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу каталога.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver

    @allure.step("Добавить товар '{item_name}' в корзину")
    def add_to_cart(self, item_name: str) -> None:
        """
        Находит кнопку добавления товара по его названию и нажимает её.

        :param item_name: Название товара (строка).
        :return: None
        """
        # Формируем ID кнопки на основе названия товара
        item_id = item_name.lower().replace(" ", "-")
        locator = (By.ID, f"add-to-cart-{item_id}")
        self.driver.find_element(*locator).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """
        Выполняет переход на страницу корзины.

        :return: None
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
