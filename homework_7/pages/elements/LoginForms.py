from selenium.webdriver.common.by import By

from ..BasePage import BasePage
from .LoginData import Admin, User


class UserLoginForm(BasePage):
    INPUT_EMAIL: tuple = (By.CSS_SELECTOR, "#input-email")
    INPUT_PASSWORD: tuple = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON: tuple = (By.CSS_SELECTOR, "input[value=Login]")

    def login_with(self):
        self._element(self.INPUT_EMAIL).send_keys(User.EMAIL)
        self._element(self.INPUT_PASSWORD).send_keys(User.PASSWORD)
        self._click(self.LOGIN_BUTTON)


class AdminLoginForm(BasePage):
    USERNAME_FIELD: tuple = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_FIELD: tuple = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BTN: tuple = (By.CSS_SELECTOR, "button[type='submit']")

    def admin_login(self):
        self._wait_element(self.USERNAME_FIELD).send_keys(Admin.LOGIN)
        self._wait_element(self.PASSWORD_FIELD).send_keys(Admin.PASSWORD)
        self._click(self.LOGIN_BTN)
