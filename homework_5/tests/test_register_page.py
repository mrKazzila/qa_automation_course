from framework import wait_element, wait_title_contain
from selenium.webdriver.common.by import By


class RegisterPage:
    ADD_URL: str = 'index.php?route=account/register'
    TITLE: str = 'Register Account'
    NAME_FIELD: tuple = (By.CSS_SELECTOR, 'input[type="text"][name="firstname"]')
    CONTINUE_BUTTON: tuple = (By.CSS_SELECTOR, 'input[type="submit"][value="Continue"]')
    PRIVACY_CHECKBOX_BTN: tuple = (By.CSS_SELECTOR, 'input[type="checkbox"][name="agree"]')
    SUBSCRIBE_BTN: tuple = (By.CSS_SELECTOR, 'input[type="radio"][name="newsletter"]')


def test_register_page_title(driver, base_url):
    driver.get(f'{base_url}{RegisterPage.ADD_URL}')
    wait_title_contain(driver, RegisterPage.TITLE)


def test_register_page_name_field(driver, base_url):
    driver.get(f'{base_url}{RegisterPage.ADD_URL}')
    wait_element(driver, RegisterPage.NAME_FIELD)


def test_register_page_subscribe_btn(driver, base_url):
    driver.get(f'{base_url}{RegisterPage.ADD_URL}')
    wait_element(driver, RegisterPage.SUBSCRIBE_BTN)


def test_register_page_continue_btn(driver, base_url):
    driver.get(f'{base_url}{RegisterPage.ADD_URL}')
    wait_element(driver, RegisterPage.CONTINUE_BUTTON)


def test_register_page_privacy_checkbox_btn(driver, base_url):
    driver.get(f'{base_url}{RegisterPage.ADD_URL}')
    wait_element(driver, RegisterPage.PRIVACY_CHECKBOX_BTN)
