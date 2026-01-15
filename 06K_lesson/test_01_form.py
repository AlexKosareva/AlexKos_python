import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_validation():
    options = EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Edge(options=options)
    
    driver.maximize_window()

    try:
        # 1. Открыть страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # 2. Заполнение формы
        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")
        
        # Поле Zip code оставляем пустым
        driver.find_element(By.NAME, "zip-code").clear()

        # 3. Нажать кнопку Submit
        wait = WebDriverWait(driver, 15) # Увеличили время ожидания до 15 сек
        submit_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        
        # Скролл и клик
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        driver.execute_script("arguments[0].click();", submit_button)

        # 4. Ожидание, пока поле Zip Code получит класс валидации (alert-danger или alert-success)
        # Ждем, пока у элемента ID 'zip-code' в атрибуте class появится слово 'alert'
        wait.until(lambda d: "alert" in d.find_element(By.ID, "zip-code").get_attribute("class"))

        # Проверка Zip code (должен быть красным)
        zip_code_class = driver.find_element(By.ID, "zip-code").get_attribute("class")
        assert "alert-danger" in zip_code_class, f"Zip code ожидался красный, но класс: {zip_code_class}"

        # 5. Проверка остальных полей (должны быть зелеными)
        fields = [
            "first-name", "last-name", "address", "e-mail", 
            "phone", "city", "country", "job-position", "company"
        ]
        
        for field_id in fields:
            field_class = driver.find_element(By.ID, field_id).get_attribute("class")
            assert "alert-success" in field_class, f"Поле {field_id} не подсвечено зеленым"

    finally:
        driver.quit()
