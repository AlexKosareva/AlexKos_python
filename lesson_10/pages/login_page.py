import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """
    Класс для работы со страницей авторизации.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу логина.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self._username = (By.ID, "user-name")
        self._password = (By.ID, "password")
        self._login_btn = (By.ID, "login-button")

    @allure.step("Авторизоваться под пользователем: {user}")
    def login(self, user: str, pwd: str) -> None:
        """
        Выполняет вход в систему под указанными учетными данными.

        :param user: Логин пользователя (строка).
        :param pwd: Пароль пользователя (строка).
        :return: None
        """
        self.driver.find_element(*self._username).send_keys(user)
        self.driver.find_element(*self._password).send_keys(pwd)
        self.driver.find_element(*self._login_btn).click()
