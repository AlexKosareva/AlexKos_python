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
    # Настройка Firefox (GeckoDriver)
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_saucedemo_purchase(driver):
    # Инициализация страниц
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Открыть сайт
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизоваться
    login_page.login("standard_user", "secret_sauce")

    # 3. Добавить товары
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_to_cart("Sauce Labs Onesie")

    # 4. Перейти в корзину и нажать Checkout
    inventory_page.go_to_cart()
    cart_page.checkout()

    # 5. Заполнить форму
    checkout_page.fill_form("Алекс", "Кос", "123456")

    # 6. Проверить итоговую стоимость
    total = checkout_page.get_total()
    print(f"\nИтоговая сумма в корзине: {total}")
    assert total == "$58.29", f"Ожидалось $58.29, но получили {total}"
