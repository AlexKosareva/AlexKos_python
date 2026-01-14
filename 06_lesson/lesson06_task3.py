from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # 1. Перейти на сайт
    driver.get(" https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # 2. Дождаться загрузки картинок
    # Ждем появления последней картинки с id="landscape", 
    # это гарантирует, что вся группа загрузилась
    waiter = WebDriverWait(driver, 20)
    waiter.until(EC.presence_of_element_located((By.ID, "landscape")))

    # 3. Находим все картинки именно в контейнере, чтобы не зацепить лишнее
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    
    # Чтобы получить 3-ю картинку, используем индекс [2]
    third_image = images[2]
    src_value = third_image.get_attribute("src")

    # 4. Вывод в консоль
    print(src_value)

finally:
    driver.quit()
