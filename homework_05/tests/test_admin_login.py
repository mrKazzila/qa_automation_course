from framework import wait_element, wait_title_contain
from selenium.webdriver.common.by import By


class AdminPage:
    ADD_URL: str = 'admin/'
    TITLE: str = 'Administration'
    USERNAME_FIELD: tuple = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_FIELD: tuple = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BTN: tuple = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_BTN: tuple = (By.CSS_SELECTOR, "span[class='help-block']")


def test_admin_page_title(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    wait_title_contain(driver, AdminPage.TITLE)


def test_admin_page_username_field(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    wait_element(driver, AdminPage.USERNAME_FIELD)


def test_admin_page_password_field(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    wait_element(driver, AdminPage.PASSWORD_FIELD)


def test_admin_page_login_btn(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    wait_element(driver, AdminPage.LOGIN_BTN)


def test_admin_page_forgotten_btn(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    wait_element(driver, AdminPage.LOGIN_BTN)
