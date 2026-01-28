from selenium import webdriver

# Selenium автоматически обнаружит Chrome 144 и скачает нужный драйвер
driver = webdriver.Chrome()

try:
    # Ваш код здесь
    driver.get("uitestingplayground.com")
finally:
    driver.quit()