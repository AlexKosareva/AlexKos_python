import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и закрытия драйвера Firefox.
    """
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.epic("Интернет-магазин")
@allure.feature("Покупка товаров")
@allure.story("Сквозной сценарий заказа (End-to-End)")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Тест покупки набора товаров")
@allure.description(
    "Авторизация, выбор 3-х товаров, заполнение формы и проверка финальной цены."
)
def test_saucedemo_purchase(driver):
    """
    Тестовый сценарий полной цепочки покупки от входа до проверки чека.
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Открыть сайт магазина"):
        driver.get("https://www.saucedemo.com/")

    login_page.login("standard_user", "secret_sauce")

    with allure.step("Выбрать товары"):
        inventory_page.add_to_cart("Sauce Labs Backpack")
        inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_to_cart("Sauce Labs Onesie")

    inventory_page.go_to_cart()
    cart_page.checkout()

    checkout_page.fill_form("Алекс", "Кос", "123456")

    with allure.step("Проверить итоговую стоимость заказа"):
        total = checkout_page.get_total()
        assert total == "$58.29", f"Ожидалось $58.29, но получили {total}"
