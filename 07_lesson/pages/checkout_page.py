from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self._first_name = (By.ID, "first-name")
        self._last_name = (By.ID, "last-name")
        self._zip_code = (By.ID, "postal-code")
        self._continue_btn = (By.ID, "continue")
        self._total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first, last, zip_code):
        self.driver.find_element(*self._first_name).send_keys(first)
        self.driver.find_element(*self._last_name).send_keys(last)
        self.driver.find_element(*self._zip_code).send_keys(zip_code)
        self.driver.find_element(*self._continue_btn).click()

    def get_total(self):
        total_text = self.driver.find_element(*self._total_label).text
        # Извлекаем только сумму, убирая текст "Total: "
        return total_text.split("Total: ")[1]
