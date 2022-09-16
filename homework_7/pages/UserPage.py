import allure
from selenium.webdriver.common.by import By

from .BasePage import BasePage
from .elements.LoginData import User


class UserPage(BasePage):
    ADD_URL: str = 'index.php?route=account/register'

    TITLE: str = 'Register Account'

    FIRST_NAME_FIELD: tuple = (By.CSS_SELECTOR, "input[type='text'][name='firstname']")
    LAST_NAME_FIELD: tuple = (By.CSS_SELECTOR, "input[type='text'][name='lastname']")
    EMAIL_FIELD: tuple = (By.CSS_SELECTOR, "input[type='email'][name='email']")
    PHONE_FIELD: tuple = (By.CSS_SELECTOR, "input[type='tel'][name='telephone']")

    PASSWORD_FIELD: tuple = (By.CSS_SELECTOR, "input[type='password'][name='password']")
    CONFIRM_PASSWORD_FIELD: tuple = (By.CSS_SELECTOR, "input[type='password'][name='confirm']")

    SUBSCRIBE_BTN: tuple = (By.CSS_SELECTOR, "input[type='radio'][name='newsletter']")
    PRIVACY_CHECKBOX_BTN: tuple = (By.CSS_SELECTOR, "input[type='checkbox'][name='agree']")
    CONTINUE_BUTTON: tuple = (By.CSS_SELECTOR, "input[type='submit'][value='Continue']")

    ACCEPT_REGISTRATION: tuple = (By.XPATH, "//h1[contains(text(),'Your Account Has Been Created!')]")

    @allure.step
    def input_user_data_in_field(self):
        self.logger.info(f'Add register information for test user')
        self._wait_element(self.FIRST_NAME_FIELD).send_keys(User.FIRST_NAME)
        self._wait_element(self.LAST_NAME_FIELD).send_keys(User.LAST_NAME)
        self._wait_element(self.EMAIL_FIELD).send_keys(User.EMAIL)
        self._wait_element(self.PHONE_FIELD).send_keys(User.PHONE)
        self._wait_element(self.PASSWORD_FIELD).send_keys(User.PASSWORD)
        self._wait_element(self.CONFIRM_PASSWORD_FIELD).send_keys(User.PASSWORD)

    @allure.step
    def click_privacy_and_continue_for_registration(self):
        self.logger.info(f'Registration test user')
        self._click(self.PRIVACY_CHECKBOX_BTN)
        self._click(self.CONTINUE_BUTTON)

    @allure.step
    def checking_registration(self):
        self.logger.info(f'Check registration')
        self._wait_element(self.ACCEPT_REGISTRATION)
