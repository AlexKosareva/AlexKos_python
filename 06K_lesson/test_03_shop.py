import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shop_total_cost():
    print("\nЗапуск браузера Firefox...")
    options = FirefoxOptions()
    # Мы убрали headless, чтобы вы видели окно. 
    # Если снова зависнет — верните options.add_argument("--headless")
    
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()

    try:
        print("Открытие сайта...")
        driver.get("https://www.saucedemo.com/")

        print("Авторизация...")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        print("Добавление товаров в корзину...")
        wait = WebDriverWait(driver, 15)
        
        # Список товаров для клика
        items = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]
        
        for item_id in items:
            wait.until(EC.element_to_be_clickable((By.ID, item_id))).click()

        print("Переход в корзину и оформление...")
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        print("Заполнение данных пользователя...")
        driver.find_element(By.ID, "first-name").send_keys("Алекс")
        driver.find_element(By.ID, "last-name").send_keys("Тестер")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        print("Проверка итоговой суммы...")
        total_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        
        total_price = total_element.text
        print(f"Найдена сумма: {total_price}")

        assert "58.29" in total_price
        print("Тест успешно завершен!")

    finally:
        driver.quit()
